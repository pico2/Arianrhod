import asyncio, socket, struct

class AsyncSocket(object):
    def __init__(self, *args, **kwargs):
        self.loop = kwargs.get('loop') or asyncio.get_event_loop()
        self.sock = socket.socket(*args, **kwargs)
        self.sock.setblocking(False)

    def setsockopt(self, *args, **kwargs):
        return self.sock.setsockopt(*args, **kwargs)

    def ioctl(self, *args, **kwargs):
        return self.sock.ioctl(*args, **kwargs)

    @asyncio.coroutine
    def connect(self, host, port):
        addrs = yield from self.loop.getaddrinfo(host, port, family = self.sock.family, type = self.sock.type, proto = self.sock.proto)

        exceptions = []
        for family, type, proto, cname, address in addrs:
            try:
                yield from self.loop.sock_connect(self.sock, address)
            except OSError as exc:
                self.sock.close()
                exceptions.append(exc)
            else:
                break

        else:
            if len(exceptions) == 1:
                raise exceptions[0]
            else:
                # If they all have the same str(), raise one.
                model = str(exceptions[0])
                if all(str(exc) == model for exc in exceptions):
                    raise exceptions[0]
                # Raise a combined exception so the user can see all
                # the various error messages.
                raise OSError('Multiple exceptions: {}'.format(
                    ', '.join(str(exc) for exc in exceptions)))

    @asyncio.coroutine
    def send(self, data):
        return self.loop.sock_sendall(self.sock, data)

    @asyncio.coroutine
    def recv(self, n):
        return self.loop.sock_recv(self.sock, n)

    @asyncio.coroutine
    def close(self):
        self.sock.close()

class QueuedAsyncSocket(AsyncSocket):
    class Task(asyncio.Future):
        def __init__(self, data, build_packet = None, read_packet = None):
            super().__init__()
            self.data = data
            self.build_packet = build_packet or QueuedAsyncSocket.build_packet
            self.read_packet = read_packet or QueuedAsyncSocket.read_packet

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.PendingTasks = asyncio.Semaphore(value = 0)
        self.Tasks = []
        self.Exit = False

        self.handle = asyncio.async(self.request_worker())

    def shutdown(self):
        self.Exit = True
        self.handle.cancel()

    @asyncio.coroutine
    def request_worker(self):
        while not self.Exit:
            yield from self.PendingTasks.acquire()
            task = self.Tasks.pop(0)
            packet = task.build_packet(task.data)
            yield from self.send(packet)
            ret = yield from task.read_packet(self)

            task.set_result(ret)

    @asyncio.coroutine
    def request(self, data, *, build_packet = None, read_packet = None):
        self.Tasks.append(self.Task(data, build_packet, read_packet))
        self.PendingTasks.release()
        return (yield from self.Tasks[-1])

    @staticmethod
    def build_packet(data):
        return struct.pack('>I', len(data)) + data

    @staticmethod
    @asyncio.coroutine
    def read_packet(sock):
        length = yield from sock.recv(4)
        length = int.from_bytes(length, 'big')
        if length == 0:
            return b''

        return (yield from sock.recv(length))
