from Crypto.Cipher import AES


def encrypts(value:str, key:str) -> tuple[bytes,bytes,bytes]:
	"""
	
	Encrypts a string using another string.
	
	Args:
		value : string to encrypt.
		key : string to use as key. Must be 16-bytes long.
	
	Returns:
		tuple(ciphertext, tag, nonce)
	
	"""
	
	cipher = AES.new(key.encode(), AES.MODE_EAX)
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
		key : string to use as key. Must be 16-bytes long.
	
	Returns:
		decrypted string.
	
	Raises:
		ValueError : message is not authentic.
	"""
	
	cipher = AES.new(key.encode(), AES.MODE_EAX, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	cipher.verify(tag)
	return plaintext.decode()


def encrypt(input_file:str, output_file:str, key:str) -> None:
	"""
	
	Encrypt a file using a string.
	
	Args:
		input_file : file to encrypt
		output_file : location where to store encrypted file
		key : string to use as key. Must be 16-bytes long.

	"""
	
	DEL = b'\x00\x01\x02\x03' \
		b'\x04\x05\x06\x07' \
		b'\x08\x09\x0a\x0b' \
		b'\x0c\x0d\x0e\x0f'
	
	with open(input_file, 'r') as f, open(output_file, 'wb') as g:
		c, t, n = encrypts(f.read(), key)
		g.write(c + DEL + t + DEL + n)


def decrypt(input_file:str, output_file:str, key:str) -> None:
	"""
	
	Decrypt a file using a string.
	
	Args:
		input_file : file to decrypt
		output_file : location where to store decrypted file
		key : string to use as key. Must be 16-bytes long.

	"""
	
	DEL = b'\x00\x01\x02\x03' \
		b'\x04\x05\x06\x07' \
		b'\x08\x09\x0a\x0b' \
		b'\x0c\x0d\x0e\x0f'
	
	with open(input_file, 'rb') as f, open(output_file, 'w') as g:
		c, t, n = f.read().split(DEL)
		g.write( decrypts(c, t, n, key) )
