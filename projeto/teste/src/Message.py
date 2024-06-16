class Message:
    def __init__(self, temp: int, humi: int):
        self.temp = temp
        self.humi = humi
        self.warning = False

    def __str__(self):
        return "Temp: %d, Humi: %d" % (self.temp, self.humi)
