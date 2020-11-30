from fernet import Fernet

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)


key = Fernet.generate_key()
print(key.decode())
message = 'John Doe'
token = encrypt(message.encode(), key)
print(token)
y = decrypt(token, key).decode()
print(y)