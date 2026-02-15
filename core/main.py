from core.encryption import Encryption
from core.decryption import Decryption
from core.sendEmail import SendEmail
from utils.sendEmail_logo import LOGO
from utils.terminated_logo import TERMINATED_LOGO
from pypdf.errors import FileNotDecryptedError
from pathlib import Path

class StartProgram:
    def __init__(self):
        self.main()

    def main(self):
        self.user_choice = input("Choose 'e' for encryption and 'd' for decryption: \n").lower()

        if self.user_choice == 'e':
            self.get_information()
            if Path(self.user_file).exists():
                if self.encrypt():
                    print(LOGO)
                    send_email = input("Do you want to send the encrypted file? 'y' for yes and 'n' for no: ").lower()
                    if send_email == 'y':
                        self.sending_email()
                    else:
                        print(TERMINATED_LOGO)
                        print("Program Terminated. File is saved. No email sent")
                else:
                    print(TERMINATED_LOGO)
                    print("No file located. Terminating Program...")
            else:
                print(TERMINATED_LOGO)
                print("No file locaed. Terminating Program...")

        elif self.user_choice == 'd':
            self.get_information()
            if Path(self.user_file).exists():
                self.decrypt()
            else:
                print(TERMINATED_LOGO)
                print("No file located. Terminating Program...")
        else:
            print(TERMINATED_LOGO)
            print("User choose to Exit")

    def encrypt(self):
        try:
            Encryption(self.user_file, self.file_password, self.user_file_name)
        except FileNotDecryptedError:
            print("File is already encrypted.")
            self.main()
        else:
            print("Encryption Success\n")
            return True

    def decrypt(self):
        Decryption(self.user_file, self.file_password, self.user_file_name)
        print("Decryption Success\n")

    def sending_email(self):
        user_email = input("Your email account: ")
        user_email_password = input("Your password: ")
        to_addrs = input("Recipient gmail address: ")
        message_content = input("Your message: ")
        subject = input("Subject: ")

        SendEmail(user_email, user_email_password, to_addrs, message_content, subject, self.file_password, self.user_file_name)
        print(f"Email Sent to {to_addrs}")

    def get_information(self):
        self.user_file = input("Input file for modification: ").strip('"')
        self.file_password = input("Input file password: ")
        self.user_file_name = input("Input where you want to save with file name (folder\\newfile.pdf): ").strip('"')