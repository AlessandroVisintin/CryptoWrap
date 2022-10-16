from CryptoWrap.hash import str2sha256

from Crypto.Cipher import AES as cAES

from pathlib import Path


# binary delimiter
DEL = b'\x00\x01\x02\x03' \
		b'\x04\x05\x06\x07' \
		b'\x08\x09\x0a\x0b' \
		b'\x0c\x0d\x0e\x0f'


def encrypts(value:str, key:str) -> tuple[bytes,bytes,bytes]:
	"""
	
	Encrypts a string using another string.
	
	Args:
		value : string to encrypt.
		key : string to use as key.
	
	Returns:
		tuple(ciphertext, tag, nonce)
	
	"""
	
	key = str2sha256(key)[:16]
	cipher = cAES.new(key.encode(), cAES.MODE_EAX)
	nonce = cipher.nonce
	ciphertext, tag = cipher.encrypt_and_digest(value.encode())
	return ciphertext, tag, nonce


def decrypts(ciphertext:bytes, tag:bytes, nonce:bytes, key:str) -> str:
	"""
	
	Decrypts a bytearray using a string.
	
	Args:
		ciphertext : bite-array to decrypt.
		tag : integrity MAC.
		nonce : encryption nonce.
		key : string to use as key.
	
	Returns:
		decrypted string.
	
	Raises:
		ValueError : message is not authentic.
	"""
	
	key = str2sha256(key)[:16]
	cipher = cAES.new(key.encode(), cAES.MODE_EAX, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	cipher.verify(tag)
	return plaintext.decode()


def encrypt(input_file:str, output_file:str, key:str) -> None:
	"""
	
	Encrypt a file using a string.
	
	Args:
		input_file : file to encrypt
		output_file : location where to store encrypted file
		key : string to use as key.

	"""
	
	input_file = Path(input_file)
	output_file = Path(output_file)
	output_parent = Path(output_file.parent)
	output_parent.mkdir(parents=True, exist_ok=True)

	key = str2sha256(key)[:16]
	cipher = cAES.new(key.encode(), cAES.MODE_EAX)	
	nonce = cipher.nonce
	
	with input_file.open('rb') as f:
		ciphertext, tag = cipher.encrypt_and_digest(f.read())
	with output_file.open('wb') as g:
		g.write(ciphertext + DEL + tag + DEL + nonce)


def decrypt(input_file:str, output_file:str, key:str) -> None:
	"""
	
	Decrypt a file using a string.
	
	Args:
		input_file : file to decrypt
		output_file : location where to store decrypted file
		key : string to use as key.

	"""
	
	input_file = Path(input_file)
	output_file = Path(output_file)
	output_parent = Path(output_file.parent)
	output_parent.mkdir(parents=True, exist_ok=True)

	with input_file.open('rb') as f:
		ciphertext, tag, nonce = f.read().split(DEL)
	
	key = str2sha256(key)[:16]
	cipher = cAES.new(key.encode(), cAES.MODE_EAX, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	cipher.verify(tag)
	
	with output_file.open('wb') as g:
		g.write(plaintext)


def encrypt_folder(folder:str, key:str) -> None:
	"""
	
	Encrypt a folder using a string.
	Output folder starts with double underscore (__).
	
	Args:
		folder : folder path.
		key : string to use as key.

	"""
	
	for i in Path(folder).glob('**/*'):
		if i.is_file():
			encrypt(f'{i}', f'__{i}', key)


def decrypt_folder(folder:str, key:str) -> None:
	"""

	Decrypt a folder using a string.
	Assumes that root folder name starts with double underscore (__).
	
	Args:
		folder : folder path.
		key : string to use as key.

	"""
	
	for i in Path(folder).glob('**/*'):
		if i.is_file():
			decrypt(f'{i}', f'{str(i)[2:]}', key)
