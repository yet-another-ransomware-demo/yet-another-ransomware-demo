# import the local core packages
from core import encrypt_file
from core import find_files
from cryptography.fernet import Fernet

def test_encrypt_file():
    # genkey
    key = Fernet.generate_key()

    # save key
    with open("key", 'wb') as f:
        f.write(key)

    # find all files and encrypt them
    files = find_files("./os_root")
    for file in files:
        print(f"encrypted {file}")
        encrypt_file(file, key)
