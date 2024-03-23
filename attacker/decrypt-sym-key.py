import rsa
import base64
import sys

def read_private_key_from_pem(file_path):
    with open(file_path, 'rb') as key_file:
        key_data = key_file.read()

    private_key = rsa.PrivateKey.load_pkcs1(key_data)
    return private_key

def decrypt_file(enc_sym_key, private_key):
    encrypted_data = enc_sym_key
    encrypted_data = base64.b64decode(encrypted_data)
    decrypted_data = rsa.decrypt(encrypted_data, private_key)
    return decrypted_data.decode('utf-8')


# Example usage:
n = len(sys.argv)
if n < 3:
    print("usage: python decrypt-sym-key.py <private-key> <key-string>")
    exit(1)
private_key = read_private_key_from_pem(sys.argv[1])
decrypted_contents = decrypt_file(sys.argv[2], private_key)
print("Decrypted contents:", decrypted_contents)
