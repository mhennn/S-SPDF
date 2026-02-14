from pypdf import PdfReader, PdfWriter

class Decryption:
    def __init__(self, encrypted_file, password, file):
        self.reader = PdfReader(encrypted_file)
        self.read_protected_file(password, file)

    def read_protected_file(self, password, file):
        if self.reader.is_encrypted:
            self.reader.decrypt(password)

        self.writer = PdfWriter(clone_from=self.reader)
        return self.save_file(file)

    def save_file(self, file_name):
        self.writer.write(file_name)