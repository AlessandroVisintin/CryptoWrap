import hashlib


def str2sha256(string:str) -> str:
	"""
	
	Get sha256 of string.
	
	Args :
		string : string to hash.
	
	Returns :
		64-byte string hexadecimal digest.
		
	
	"""
	
	return hashlib.sha256(string.encode('utf-8')).hexdigest()
