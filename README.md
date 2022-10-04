# CryptoWrap
> Helper functions to perform cryptographic operations.

CryptoWrap contains cryptographic modules for performing cryptographic operations.

## Installation
Clone the project inside your working directory.
You can use it right away by adding the cloned folder into sys.path.
You can also install the package locally by running pip at the root level.
```sh
pip install /path/to/root/level
```

## Usage examples
Encrypt using AES.
```py

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
PLAIN = 'config/CryptoWrap/plain.txt'
CIPHER = 'config/CryptoWrap/cipher.txt'
DECRYP = 'config/CryptoWrap/decryp.txt'

print('Encrypting ', PLAIN)
encrypt(PLAIN, CIPHER, KEY)

print('Decrypting ', CIPHER)
decrypt(CIPHER, DECRYP, KEY)

```

## Meta
Alessandro Visintin - alevise.public@gmail.com

Find me: [Twitter](https://twitter.com/analog_cs) [Medium](https://medium.com/@analog_cs)

Distributed under the MIT license. See ``LICENSE.txt``.
