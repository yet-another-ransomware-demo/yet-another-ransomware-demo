from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import rsa


def encrypt_file(file_path, key):

    """
    Encrypts the content of a file using symmetric encryption and replaces the
    original file with the encrypted content.

    Args:
    - file_path (str): The path to the file to be encrypted.
    - key (bytes): The encryption key to be used.

    Returns:
    - None
    """
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

        print(f"File '{file_path}' encrypted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def load_key_from_file(file_path):
    """
    Loads the encryption key from a file.

    Args:
    - file_path (str): The path to the file containing the key.

    Returns:
    - bytes: The encryption key.
    """
    try:
        with open(file_path, 'rb') as f:
            key = f.read()
        return key
    except FileNotFoundError:
        print(f"Key file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while loading the key: {e}")
    return None


def decrypt_file(file_path, key):

    """
    Decrypts the content of a file using symmetric encryption and replaces the
    original file with the decrypted content.

    Args:
    - file_path (str): The path to the file to be decrypted.
    - key (bytes): The encryption key.

    Returns:
    - None
    """

    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

        print(f"File '{file_path}' decrypted and replaced successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def encrypt_symmetric_key(sym_key, public_key_filepath="public_key.pem"):
    """
    Given a sym key and a public key, encrypts the sym key with the public key
    Note that the sym key needs to be in bytes
    """
    # read the public key
    with open(public_key_filepath, "rb") as key_file:
        public_key_data = key_file.read()
        public_key = rsa.key.PublicKey.load_pkcs1(public_key_data)
        enc_sym_key = rsa.encrypt(sym_key, public_key)
        return enc_sym_key
