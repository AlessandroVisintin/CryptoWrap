from CryptoWrap.AES import encrypts
from CryptoWrap.AES import decrypts
from CryptoWrap.AES import encrypt
from CryptoWrap.AES import decrypt


# encrypt a string
VALUE, KEY = 'My Secret Text', 'My Secret Key!!!'

print('Plain : ', VALUE)

c, t, n = encrypts(VALUE, KEY)
print('Cipher : ', c)

p = decrypts(c, t, n, KEY)
print('Plain : ', p)


# encrypt a file
PLAIN = 'out/CryptoWrap/plain.txt'
CIPHER = 'out/CryptoWrap/test1/cipher.txt'
DECRYP = 'out/CryptoWrap/test2/decrypt.txt'

print('Encrypting ', PLAIN)
encrypt(PLAIN, CIPHER, KEY)

print('Decrypting ', CIPHER)
decrypt(CIPHER, DECRYP, KEY)
