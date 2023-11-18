from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from base64 import b64encode, b64decode
import getpass
def encrypt_pbe_with_md5_and_des(password, plaintext):
    # Generate a random 8-byte salt
    salt = get_random_bytes(8)

    # Derive a key using PBKDF2 with MD5
    key = PBKDF2(password, salt, 8, 1000,None)

    # Create a DES cipher object with CBC mode
    cipher = DES.new(key, DES.MODE_CBC)

    # Pad the plaintext to be a multiple of 8 bytes
    padded_plaintext = plaintext + (8 - len(plaintext) % 8) * chr(8 - len(plaintext) % 8)

    # Encrypt the padded plaintext
    ciphertext = cipher.iv + cipher.encrypt(padded_plaintext.encode('utf-8'))

    # Combine salt and ciphertext for storage or transmission
    encrypted_data = salt + ciphertext

    # Base64 encode for easy storage or transmission
    return b64encode(encrypted_data).decode('utf-8')

def decrypt_pbe_with_md5_and_des(password, encrypted_text):
    # Base64 decode to get the salt and ciphertext
    encrypted_data = b64decode(encrypted_text.encode('utf-8'))
    salt = encrypted_data[:8]
    ciphertext = encrypted_data[8:]

    # Derive a key using PBKDF2 with MD5
    key = PBKDF2(password, salt, 8, 1000, None)

    # Create a DES cipher object with CBC mode
    cipher = DES.new(key, DES.MODE_CBC,ciphertext[:8])

    # Decrypt the ciphertext and remove padding
    decrypted_text = cipher.decrypt(ciphertext[8:]).decode('utf-8')
    padding_length = ord(decrypted_text[-1])
    decrypted_text = decrypted_text[:-padding_length]

    return decrypted_text

