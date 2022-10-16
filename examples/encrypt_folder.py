"""

Encrypt a folder.
Output folder starts with double underscore (__).

"""

from CryptoWrap.AES import encrypt

from pathlib import Path


inp = input('Relative path to input folder: ')
key = input('Key to encrypt: ')

for i in Path(inp).glob('**/*'):
	if i.is_file():
		encrypt(f'{i}', f'__{i}', key)
