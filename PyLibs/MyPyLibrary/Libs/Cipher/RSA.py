import rsa
from pyasn1.type.error import PyAsn1Error

class RsaCipher:
    def __init__(self, key):
        try:
            self.key = rsa.key.PublicKey.load_pkcs1(key, 'DER')
            self.encrypt = self.public_encrypt
            self.decrypt = self.public_decrypt

        except PyAsn1Error:
            self.key = rsa.key.PrivateKey.load_pkcs1(key, 'DER')
            self.encrypt = self.private_encrypt
            self.decrypt = self.private_decrypt

        self.DecryptBlockSize = rsa.common.byte_size(self.key.n)
        self.EncryptBlockSize = self.DecryptBlockSize - 11

    def public_encrypt(self, message, *, encoding = 'UTF8'):
        if isinstance(message, str):
            message = message.encode('UTF8')

        crypto = bytearray()
        for start in range(0, len(message), self.EncryptBlockSize):
            crypto.extend(rsa.encrypt(message[start : start + self.EncryptBlockSize], self.key))

        return crypto

    def private_decrypt(self, crypto, *, encoding = None):
        message = bytearray()
        for start in range(0, len(crypto), self.DecryptBlockSize):
            message.extend(rsa.decrypt(crypto[start : start + self.DecryptBlockSize], self.key))

        return encoding is None and message or message.decode(encoding)

    def private_encrypt(self, message):
        keylength = self.DecryptBlockSize
        padded = rsa.pkcs1._pad_for_encryption(message, keylength)

        payload = rsa.transform.bytes2int(padded)
        encrypted = rsa.core.encrypt_int(payload, self.key.d, self.key.n)
        block = rsa.transform.int2bytes(encrypted, keylength)

        return block

    def public_decrypt(self, crypto):
        blocksize = self.DecryptBlockSize
        encrypted = rsa.transform.bytes2int(crypto)
        decrypted = rsa.core.decrypt_int(encrypted, self.key.e, self.key.n)
        cleartext = rsa.transform.int2bytes(decrypted, blocksize)

        # If we can't find the cleartext marker, decryption failed.
        if cleartext[0:2] != b'\x00\x02':
            raise rsa.DecryptionError('Decryption failed')

        # Find the 00 separator between the padding and the message
        try:
            sep_idx = cleartext.index(b'\x00', 2)
        except ValueError:
            raise rsa.DecryptionError('Decryption failed')

        return cleartext[sep_idx+1:]
