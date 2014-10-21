import base64

class AesCipher:
    def __init__(self, key, iv = None, *, Fast = False, Secret = 0):

        if Fast:
            from Crypto.Cipher import AES
            self.aes = AES.new(key, AES.MODE_CBC, iv or b'\x00' * 16)
            self.encrypt_block = self.fast_aes_encrypt_block
            self.decrypt_block = self.fast_aes_decrypt_block

        else:
            import pyaes
            self.aes = pyaes.AESModeOfOperationCBC(key, iv)
            self.encrypt_block = self.slow_aes_encrypt_block
            self.decrypt_block = self.slow_aes_decrypt_block

        self.DecryptBlockSize = 16
        self.EncryptBlockSize = 16
        self.Secret = Secret

    def encrypt(self, message, *, encoding = 'UTF8'):
        if isinstance(message, str):
            message = message.encode('UTF8')

        crypto = bytearray()
        pad = self.EncryptBlockSize - len(message) % self.EncryptBlockSize
        for start in range(0, len(message), self.EncryptBlockSize):
            crypto.extend(self.encrypt_block(message[start : start + self.EncryptBlockSize]))

        crypto.append(pad ^ self.Secret)
        return crypto

    def decrypt(self, crypto, *, encoding = None):
        message = bytearray()
        pad = crypto[-1] ^ self.Secret
        crypto = crypto[:-1]
        for start in range(0, len(crypto), self.DecryptBlockSize):
            message.extend(self.decrypt_block(crypto[start : start + self.DecryptBlockSize]))

        if pad != 0:
            message[-pad:] = []

        return encoding is None and message or message.decode(encoding)

    def encryptstring(self, string, *, encoding = 'UTF8'):
        return base64.encodebytes(self.encrypt(string.encode(encoding))).decode('ASCII')

    def decryptstring(self, crypto, *, encoding = 'UTF8'):
        return self.decrypt(base64.decodebytes(crypto.encode('ASCII'))).decode(encoding)

    def slow_aes_encrypt_block(self, message):
        pad = 0
        if len(message) < self.EncryptBlockSize:
            pad = self.EncryptBlockSize - len(message)
            message = message + b'\x00' * pad

        return self.aes.encrypt(message)

    def slow_aes_decrypt_block(self, crypto):
        return self.aes.decrypt(crypto)

    def fast_aes_encrypt_block(self, message):
        return self.slow_aes_encrypt_block(bytes(message))

    def fast_aes_decrypt_block(self, crypto):
        return self.slow_aes_decrypt_block(bytes(crypto))
