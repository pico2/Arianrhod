import rsa
from pyasn1.type.error import PyAsn1Error

class RsaCipher:
    def __init__(self, key):
        try:
            self.key = rsa.key.PublicKey.load_pkcs1(key, 'DER')
            self.encryptor = self.public_encryptor
            self.decryptor = self.public_decryptor

        except PyAsn1Error:
            self.key = rsa.key.PrivateKey.load_pkcs1(key, 'DER')
            self.encryptor = self.private_encryptor
            self.decryptor = self.private_decryptor

        self.DecryptBlockSize = rsa.common.byte_size(self.key.n)
        self.EncryptBlockSize = self.DecryptBlockSize - 11

    def encrypt(self, message, *, encoding = 'UTF8'):
        if isinstance(message, str):
            message = message.encode('UTF8')

        crypto = bytearray()
        for start in range(0, len(message), self.EncryptBlockSize):
            crypto.extend(self.encryptor(message[start : start + self.EncryptBlockSize], self.key))

        return crypto

    def decrypt(self, crypto, *, encoding = None):
        message = bytearray()
        for start in range(0, len(crypto), self.DecryptBlockSize):
            message.extend(self.decryptor(crypto[start : start + self.DecryptBlockSize], self.key))

        return encoding is None and message or message.decode(encoding)

    def private_decryptor(self, crypto, key):
        return rsa.decrypt(crypto, key)

    def private_encryptor(self, message, key):
        pub = rsa.key.PublicKey(n = key.n, e = key.d)
        return rsa.encrypt(message, pub)

    def public_encryptor(self, message, key):
        return rsa.encrypt(message, key)

    def public_decryptor(self, crypto, key):
        private = rsa.key.PrivateKey(n = key.n, e = 0, d = key.e, p = 0, q = 0, exp1 = 0, exp2 = 0, coef = 0)
        return rsa.decrypt(crypto, private)
