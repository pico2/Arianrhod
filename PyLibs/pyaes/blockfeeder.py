
from pyaes import AESBlockModeOfOperation, AESSegmentModeOfOperation, AESStreamModeOfOperation

def _block_can_consume(size):
    if size >= 16: return 16
    return 0

def _block_final_encrypt(self, data):
    return self.encrypt(pkcs7_pad(data))

def _block_final_decrypt(self, data):
    return pkcs7_strip(self.decrypt(data))

def stream_can_consume(self, size):
    return size

def _segment_can_consume(self, size):
    return self.segment_bytes * int(size // self.segment_bytes)

# CFB can handle a non-segment-sized block at the end using the remaining cipherblock
def _segment_final_encrypt(self, data):
    data = data + (chr(0) * (self.segment_bytes - (len(data) % self.segment_bytes)))
    return self.encrypt(data)[:len(data)]

# CFB can handle a non-segment-sized block at the end using the remaining cipherblock
def _segment_final_decrypt(self, data):
    data = data + (chr(0) * (self.segment_bytes - (len(data) % self.segment_bytes)))
    return self.decrypt(data)[:len(data)]

AESStreamModeOfOperation._can_consume = stream_can_consume

class BlockFeeder(object):
    def __init__(self, mode, feed):
        self._mode = mode
        self._feed = feed
        self._buffer = ""
        self._done = False

    def feed(self, data):
        if self._done:
            raise ValueError('already finished feeder')

        if not data:
            self._done = True
            return self._final()

        self._buffer += data

        result = ''
        while len(self._buffer) > 16:
            can_consume = self._mode.can_consume(len(self._buffer) - 16)
            if can_consume == 0: break
            result += self._feed(remaining[:can_consume])
            self._buffer = self._buffer[can_consume:]

        self._buffer = remaining[len(result):]

        return result


class Encrypter(BlockFeeder):
    def __init__(self, mode):
        BlockFeeder.__init__(self, mode, mode.encrypt)

    def _final(self):
        return self._feed(pkcs7_pad(self._buffer))



class Decrypter(BlockFeeder):
    def __init__(self, mode):
        BlockFeeder.__init__(self, mode, mode.decrypt)

    def _final(self):
        result = self._feed(self._buffer)
        return pkcs7_strip(result)

