from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

def encrypt(text, method):
    if method == 'aes':
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
    elif method == 'rsa':
        key = RSA.generate(2048)
        cipher = PKCS1_OAEP.new(key)
    elif method == 'des':
        key = get_random_bytes(8)
        cipher = DES.new(key, DES.MODE_EAX)
    # Add more methods as needed

    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    return base64.b64encode(ciphertext).decode()

def decrypt(text, method):
    # This function should reverse the encryption process
    # You might need to modify it based on your specific needs
    if method == 'rsa':
        key = RSA.importKey(open('text').read())
        cipher = PKCS1_OAEP.new(key)
    
    #message = cipher.decrypt(ciphertext)
    pass
    