import asyncio, socket, struct, ssl

class AsyncSocket(object):
    def __init__(self, *args, **kwargs):
        try:
            keyfile         = kwargs.pop('keyfile')
            certfile        = kwargs.pop('certfile')
            SSL             = kwargs.pop('ssl')
            self.sslContext = kwargs.pop('sslContext')
        except KeyError:
            SSL = False
            self.sslContext = None

        self.loop = kwargs.get('loop') or asyncio.get_event_loop()
        self.sock = socket.socket(*args, **kwargs)
        self.sock.setblocking(False)

        if not SSL:
            return

        if self.sslContext is None:
            self.sslContext = ssl._create_stdlib_context(certfile = certfile, keyfile = keyfile)

    def __del__(self):
        self.close()

    def setsockopt(self, *args, **kwargs):
        return self.sock.setsockopt(*args, **kwargs)

    def ioctl(self, *args, **kwargs):
        return self.sock.ioctl(*args, **kwargs)

    @asyncio.coroutine
    def connect(self, host, port):
        addrs = yield from self.loop.getaddrinfo(host, port, family = self.sock.family, type = self.sock.type, proto = self.sock.proto)

        if self.sslContext is not None and not isinstance(self.sock, ssl.SSLSocket):
            self.sock = self.sslContext.wrap_socket(self.sock, server_hostname = host)

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
        return (yield from self.loop.sock_sendall(self.sock, data))

    @asyncio.coroutine
    def recv(self, n):
        data = bytearray()
        while n > 0:
            ret = yield from self.loop.sock_recv(self.sock, n)
            if not ret:
                break

            data.extend(ret)
            n -= len(ret)

        return data

    @asyncio.coroutine
    def close(self):
        self.sock.close()

class QueuedAsyncSocket(AsyncSocket):
    class Task(asyncio.Future):
        def __init__(self, data, buildPacket = None, readPacket = None):
            super().__init__()
            self.data = data
            self.buildPacket = buildPacket or QueuedAsyncSocket.buildPacket
            self.readPacket = readPacket or QueuedAsyncSocket.readPacket

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
            packet = task.buildPacket(task.data)
            yield from self.send(packet)
            ret = yield from task.readPacket(self)

            task.set_result(ret)

    @asyncio.coroutine
    def request(self, data, *, buildPacket = None, readPacket = None):
        task = self.Task(data, buildPacket, readPacket)
        self.Tasks.append(task)
        self.PendingTasks.release()
        return (yield from task)

    @staticmethod
    def buildPacket(data):
        return struct.pack('>I', len(data)) + data

    @staticmethod
    @asyncio.coroutine
    def readPacket(sock):
        length = yield from sock.recv(4)
        length = int.from_bytes(length, 'big')
        if length == 0:
            return b''

        return (yield from sock.recv(length))
