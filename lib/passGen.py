import secrets
def passGen():
	password = secrets.token_hex(5)
	return password
