from Message import Message

class Logger:
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages
    
    def clear_messages(self):
        self.messages = []

    def get_messages_by_state(self, state):
        return [message for message in self.messages if message.state == state]
    
    def get_messages_by_name(self, name):
        return [message for message in self.messages if message.name == name]
    
    def get_messages_by_name_and_state(self, name, state):
        return [message for message in self.messages if message.name == name and message.state == state]