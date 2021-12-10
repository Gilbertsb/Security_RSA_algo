from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP   #You have to install conda install pycryptodome to have those library
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
#print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
#print(pubKeyPEM.decode('ascii'))

#print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
#print(privKeyPEM.decode('ascii'))


msg = bytes(str(input("Enter plain text: ")), 'utf-8')
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)       #encyrpting message
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)      #decyrpting message
print('Decrypted:', decrypted.decode('utf-8'))







