import ssd1306
from machine import I2C # type: ignore

class Display:
    def __init__(self):
        __OLED_WIDTH = 128
        __OLED_HEIGHT = 64
        __I2C = I2C(0, mode=I2C.MASTER, pins=('G21','G22'), baudrate=100000)
        self.oled = ssd1306.SSD1306_I2C(__OLED_WIDTH, __OLED_HEIGHT, __I2C)

    def showData(self, message):
        self.oled.fill(0)
        self.oled.text("Temp: %d C" % message.temp, 0, 0)
        self.oled.text("Humi: %d %%" % message.humi, 0, 10)

        if message.temp_warning == 1:
            self.oled.text("High Temp!", 0, 20, 1, 1)
        elif message.temp_warning == -1:
            self.oled.text("Low Temp!", 0, 20, 1, 1)
        if message.humi_warning == 1:
            self.oled.text("High Humi!", 0, 30)
        elif message.humi_warning == -1:
            self.oled.text("Low Humi!", 0, 30) 
                       
        self.oled.show()

    
