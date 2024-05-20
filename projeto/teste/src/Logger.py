from Message import Message
import os

DIR_PATH = "../out/"

class Logger:
    def __init__(self, file_name):
        self.file_name = DIR_PATH + file_name

    def log(self, message):
        with open(self.file_name, "a") as file:
            file.write(message + "\n")

    def get_messages(self):
        with open(self.file_name, "r") as file:
            return file.readlines()
    
    def clear_messages(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)