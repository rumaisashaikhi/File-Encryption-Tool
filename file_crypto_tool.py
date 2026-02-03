from cryptography.fernet import Fernet

# ========== KEY GENERATION ==========
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Secret key generated!")

# ========== ENCRYPT FILE ==========
def encrypt_file(filename):
    key = open("secret.key", "rb").read()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(filename, "wb") as file:
        file.write(encrypted)

    print("File encrypted successfully!")

# ========== DECRYPT FILE ==========
def decrypt_file(filename):
    key = open("secret.key", "rb").read()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted)

    print("File decrypted successfully!")

# ========== MENU ==========
print("\n🔐 FILE ENCRYPTION TOOL")
print("1. Generate Key")
print("2. Encrypt File")
print("3. Decrypt File")

choice = input("Choose option: ")

if choice == "1":
    generate_key()

elif choice == "2":
    file_name = input("Enter file name: ")
    encrypt_file(file_name)

elif choice == "3":
    file_name = input("Enter file name: ")
    decrypt_file(file_name)

else:
    print("Invalid choice")
