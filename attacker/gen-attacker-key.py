import rsa


def generate_keypair():
    # Generate RSA key pair
    (pub_key, priv_key) = rsa.newkeys(2048)
    return pub_key, priv_key


def save_key_to_file(key, file_name):
    # Save key to file
    with open(file_name, 'wb') as key_file:
        key_data = key.save_pkcs1(format='PEM')
        key_file.write(key_data)


def read_key_from_file(file_name):
    # Read key from file
    with open(file_name, 'rb') as key_file:
        key_data = key_file.read()
        key = rsa.key.PrivateKey.load_pkcs1(key_data)
    return key


# Generate key pairs
public_key, private_key = generate_keypair()

# Save keys to files
save_key_to_file(public_key, "public_key.pem")
save_key_to_file(private_key, "private_key.pem")
