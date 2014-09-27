import asyncio, socket

class AsyncSocket(object):
    def __init__(self, *args, **kwargs):
        self.loop = kwargs.get('loop') or asyncio.get_event_loop()
        self.sock = socket.socket(*args, **kwargs)
        self.sock.setblocking(False)

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

if __name__ == '__main__':
    from ml import *

    @asyncio.coroutine
    def main2():

        data = {
            "action": "AddItem",
            "data": {
                "orderid": 792362336014872,
                "buyer": "nickname",
                "seller": "nickname",
                "phone": 1234567,
                "address": "street",
                "date": "2014-07-07",
                "itemurl": "http",
            }
        }

        data = json.dumps(data).encode('UTF8')

        sock = AsyncSocket()

        print('connect')
        yield from sock.connect('localhost', 8997)

        print('send')
        yield from sock.send(struct.pack('>I', len(data)) + data)

        print('recv')
        # PauseConsole()
        r = yield from sock.recv(1000)
        print(r)

    def main():
        print('main')

        asyncio.set_event_loop(asyncio.ProactorEventLoop())
        l = asyncio.get_event_loop()
        l.run_until_complete(main2())

        print('main end')
        PauseConsole('done')

    TryInvoke(main)
