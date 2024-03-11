# import the local core packages
from core import decrypt_file, load_key_from_file
from core import find_files

def test_crypt_file():
    # load key from file
    l_key = load_key_from_file("key")

    # decrypt all files that were encrypted
    files = find_files("./os_root")
    for file in files:
        print(f"decrypted {file}")
        decrypt_file(file, l_key)
