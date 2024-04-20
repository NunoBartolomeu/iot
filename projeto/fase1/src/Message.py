class Message:
    def __init__(self, timestamp, name, value, state, difference):
        self.timestamp = timestamp
        self.name = name
        self.value = value
        self.state = state
        self.difference = difference