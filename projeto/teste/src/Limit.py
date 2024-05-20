from Message import Message

class Limit:
    def __init__(self, name: str, ideal: int, min_value: int, max_value):
        if name not in ['T', 'H']:
            raise ValueError("Invalid name. Name can only be 'T' or 'H'.")
        self.name = name 
        self.ideal = ideal
        self.min = min_value
        self.max = max_value
        if self.min > self.max:
            raise ValueError("Invalid limits.")

    def check(self, message: Message):
        if self.name == 'T':
            if message.temp < self.min:
                message.temp_warning = -1
            elif message.temp > self.max:
                message.temp_warning = 1
        elif self.name == 'H':
            if message.humi < self.min:
                message.humi_warning = -1
            elif message.humi > self.max:
                message.humi_warning = 1
        return message