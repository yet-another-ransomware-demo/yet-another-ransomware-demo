import rsa
import base64

def read_private_key_from_pem(file_path):
    with open(file_path, 'rb') as key_file:
        key_data = key_file.read()

    private_key = rsa.PrivateKey.load_pkcs1(key_data)
    return private_key


def decrypt_file(file_path, private_key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        encrypted_data = base64.b64decode(encrypted_data)
        decrypted_data = rsa.decrypt(encrypted_data, private_key)
        return decrypted_data.decode('utf-8')


# Example usage:
private_key = read_private_key_from_pem('private_key.pem')
decrypted_contents = decrypt_file('../ransomware/key', private_key)
print("Decrypted contents:", decrypted_contents)
