from pypdf import PdfReader, PdfWriter

class Encryption:
    def __init__(self, file, password, file_name):
        self.reader = PdfReader(file)
        self.writer = PdfWriter(clone_from=self.reader)
        self.create_password(password, file_name)

    def create_password(self, password, file):
        self.writer.encrypt(password, algorithm="AES-256")
        return self.save_file(file)

    def save_file(self, file):
        with open(file, "wb") as file:
            self.writer.write(file)