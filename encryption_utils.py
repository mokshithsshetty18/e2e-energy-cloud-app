from cryptography.fernet import Fernet

def generate_key():
    """Generates a new Fernet key."""
    return Fernet.generate_key().decode()

def encrypt_message(message: str, key: str) -> str:
    """Encrypts a message using the provided key."""
    f = Fernet(key.encode())
    return f.encrypt(message.encode()).decode()

def decrypt_message(token: str, key: str) -> str:
    """Decrypts a message using the provided key."""
    try:
        f = Fernet(key.encode())
        return f.decrypt(token.encode()).decode()
    except Exception as e:
        return f"Error: {str(e)}"
