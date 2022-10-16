"""

Decrypt a folder.
It assumes that root folder name starts with double underscore (__).

"""

from CryptoWrap.AES import decrypt

from pathlib import Path


inp = input('Relative path to input folder: ')
key = input('Key to decrypt: ')

for i in Path(inp).glob('**/*'):
	if i.is_file():
		decrypt(f'{i}', f'{str(i)[2:]}', key)
