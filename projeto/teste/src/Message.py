class Message:
    def __init__(self, timestamp, temp, humi):
        self.timestamp = timestamp
        self.temp = temp
        self.humi = humi
        self.temp_warning = 0
        self.humi_warning = 0

    def __str__(self):
        return "Timestamp: %d, Temp: %d, Humi: %d" % (self.timestamp, self.temp, self.humi)

    def toBits(self):
        pass