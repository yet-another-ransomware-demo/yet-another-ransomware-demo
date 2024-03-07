# Yet Another Ransomware Demo (YARD)

This project serves as a research for ransomware

## Dependencies
This project assumes that the host system you're running on is a Linux based operating system with x86 cpu architecture
For MacOS users, please run a Virtual Machine to emulate the x86 environment
- Python


## Usage
Note that by default, this project will run the `ransomware` demo against the `os_root` directory in its current directory
```sh
# to run the demo
make run
```

## Testing
To test the core features of the encryption, run the following with make:
```sh
# to test the encryption
make test-encryption

# to test the decryption
make test-decryption
```

## Building
The project uses `pyinstaller` to build the python script as a binary
```sh
make build
```
