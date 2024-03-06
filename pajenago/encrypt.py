from cryptography.fernet import Fernet
import os


def load_or_generate_key(key_file='key.key'):
    if os.path.exists(key_file):
        
        with open(key_file, 'rb') as f:
            key = f.read()
    else:
        
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return key


def encrypt_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    with open(input_file_path, 'rb') as f:
        data = f.read()
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_file_path, 'wb') as f:
        f.write(encrypted_data)
    
    os.remove(input_file_path)

def main():

    base_dir = 'C:/Users/alber/Documents/pajenago/'
    docs_dir = os.path.join(base_dir, 'docs')
    images_dir = base_dir

    
    if not os.path.exists(docs_dir):
        print(f"Directory {docs_dir} does not exist.")
        return

    
    key = load_or_generate_key()

    
    input_doc_path = os.path.join(docs_dir, 'doc.txt')
    encrypted_doc_path = os.path.join(docs_dir, 'doc_encrypted.txt')
    encrypt_file(input_doc_path, encrypted_doc_path, key)


    input_dat_path = os.path.join(docs_dir, 'dat.txt')
    encrypted_dat_path = os.path.join(docs_dir, 'dat_encrypted.txt')
    encrypt_file(input_dat_path, encrypted_dat_path, key)

    
    input_image_path = os.path.join(images_dir, 'lee4.jpg')
    encrypted_image_path = os.path.join(images_dir, 'lee4_encrypted.jpg')
    encrypt_file(input_image_path, encrypted_image_path, key)

    
    input_image_path = os.path.join(images_dir, 'leekuanyew.jpg')
    encrypted_image_path = os.path.join(images_dir, 'leekuanyew_encrypted.jpg')
    encrypt_file(input_image_path, encrypted_image_path, key)

    
    input_image_path = os.path.join(images_dir, 'leeqoute.jpg')
    encrypted_image_path = os.path.join(images_dir, 'leeqoute_encrypted.jpg')
    encrypt_file(input_image_path, encrypted_image_path, key)

if __name__ == "__main__":
    main()
