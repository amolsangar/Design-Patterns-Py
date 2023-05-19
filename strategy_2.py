from abc import ABC, abstractmethod
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

from Crypto.Cipher import Blowfish
from struct import pack

# =============================================
class IEncryptionStrategy(ABC):
    @abstractmethod
    def encrypt_data(self):
        pass

class AESEncrptionStrategy(IEncryptionStrategy):
    def __init__(self, key) -> None:
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt_data(self, plaintext):
        raw = self._pad(plaintext)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))
    
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
        
class BlowfishEncryptionStrategy(IEncryptionStrategy):
    def __init__(self,key) -> None:
        self.key = key
    
    def encrypt_data(self,plaintext):
        bs = Blowfish.block_size
        iv = Random.new().read(bs)
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
        plaintext = b'docendo discimus '
        plen = bs - divmod(len(plaintext),bs)[1]
        padding = [plen]*plen
        padding = pack('b'*plen, *padding)
        msg = iv + cipher.encrypt(plaintext + padding)
        return msg
    
# =============================================
class Encryptor:
    def __init__(self,strategy) -> None:
        self.plaintext = None
        self.strategy = strategy

    def encrypt(self, plaintext):
        return self.strategy.encrypt_data(plaintext)

    def get_plaintext(self):
        return self.plaintext
    
    def set_plaintext(self,plaintext):
        self.plaintext = plaintext

# =============================================
# Client
key = 'An arbitrarily long key'
plaintext = "sample text to test encrpytion"
print("Plaintext:",plaintext)

aes = AESEncrptionStrategy(key)
aes_encryptor = Encryptor(aes)
encrypted_text1 = aes_encryptor.encrypt(plaintext)
print("AES Encryption:",encrypted_text1)

blowfish = BlowfishEncryptionStrategy(key.encode('utf-8'))
blowfish_encryptor = Encryptor(blowfish)
encrypted_text2 = blowfish_encryptor.encrypt(plaintext.encode('utf-8'))
print("Blowfish Encryption:",encrypted_text2)