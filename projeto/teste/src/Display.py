import ssd1306
from machine import I2C # type: ignore
from Message import Message

class Display:
    def __init__(self):
        __OLED_WIDTH = 128
        __OLED_HEIGHT = 64
        __I2C = I2C(0, mode=I2C.MASTER, pins=('G21','G22'), baudrate=100000)
        self.oled = ssd1306.SSD1306_I2C(__OLED_WIDTH, __OLED_HEIGHT, __I2C)

    def showInfo(self, text):
        self.oled.fill(0)
        self.oled.text(text, 0, 15)

    def showData(self, message: Message, TEMP_LIMITS, HUMI_LIMITS):
        self.oled.fill(0)
        self.oled.text("Temp: %d C" % message.temp, 0, 0)
        self.oled.text("Humi: %d %%" % message.humi, 0, 10)

        if message.warning:
            if message.temp > TEMP_LIMITS.max:
                self.oled.text("High Temperature!", 0, 20, 1, 1)
            elif message.temp < TEMP_LIMITS.min:
                self.oled.text("Low Temperature!", 0, 20, 1, 1)
            elif message.humi > HUMI_LIMITS.max:
                self.oled.text("High Humidity!", 0, 30)
            elif message.humi < HUMI_LIMITS.min:
                self.oled.text("Low Humidity!", 0, 30) 
                       
        self.oled.show()

    
