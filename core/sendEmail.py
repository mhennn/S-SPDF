import smtplib
from pathlib import Path
from email.message import EmailMessage

class SendEmail:
    def __init__(self, user_email, user_password, to_addrs, content, subject, password, file):
        self.msg = EmailMessage()
        self.msg['Subject'] = subject
        self.msg['From'] = user_email
        self.msg['To'] = to_addrs
        self.user_email = user_email
        self.user_password = user_password
        self.user_file = file
        self.msg.set_content(f"{content}\nPassword: {password}")
        self.read_file()
            
    def read_file(self):
        self.file_path = self.user_file
        with open(self.file_path, "rb") as pdf_file:
            self.data = pdf_file.read()
            self.file_name = pdf_file.name
        
        return self.add_attachment(self.data, self.file_name)
        
    def add_attachment(self, data, file_name):
        self.msg.add_attachment(
            data,
            maintype="application",
            subtype="pdf",
            filename = Path(file_name).name
        )
        return self.sending_email()
    
    def sending_email(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.user_email, password=self.user_password)
            connection.send_message(self.msg)