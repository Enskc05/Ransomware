import os
from cryptography.fernet import Fernet

user_input_key = input("Enter the key: ")


try:
    Fernet(user_input_key)
except Exception as e:
    print("Invalid key. Exiting...")
    exit()

file_list = [file for file in os.listdir() if file not in ["ransom.py", "generatedkey.key", "main.py"] and os.path.isfile(file)]

with open("generatedkey.key", "rb") as generatedkey:
    secretkey = generatedkey.read()

cipher = Fernet(user_input_key)

for file in file_list:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    try:
        contents_decrypted = cipher.decrypt(contents)
        with open(file, "wb") as the_file:
            the_file.write(contents_decrypted)
        print(f"{file} decrypted successfully.")
    except Exception as e:
        print(f"Error decrypting {file}: {e}")
