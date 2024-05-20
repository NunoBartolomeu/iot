print("Running main")

import sys
sys.path.append('./src')

import time
from machine import Pin, I2C, ADC # type: ignore
from dht import DHT
from Display import Display
from Logger import Logger
from Message import Message
from Actuators import Actuators
from boot import TEMP_LIMITS, HUMI_LIMITS


display = Display()
dht = DHT(Pin('G2', mode=Pin.OPEN_DRAIN),0)
vcc = Pin('G13', mode=Pin.OUT)
vcc.value(1)
logger = Logger("log.txt")

SLEEP_TIME = 5

while True:
    result = dht.read()
    if result.is_valid():
        message = Message(0, result.temperature, result.humidity)
        TEMP_LIMITS.check(message)
        HUMI_LIMITS.check(message)

        if message.temp_warning != 0 or message.humi_warning != 0:
            SLEEP_TIME = 2
        else:
            SLEEP_TIME = 5

        display.showData(message)
        print(message)
        #logger.log(message)
    else:
        print("Error: %d" % result.error_code)
    time.sleep(SLEEP_TIME)


fan_pin = Pin('G14', mode=Pin.OUT)
heater_pin = Pin('G25', mode=Pin.OUT)
window_pin = Pin('G33', mode=Pin.OUT)
sprinkler_pin = Pin('G32', mode=Pin.OUT)

actuators = Actuators(fan_pin, heater_pin, window_pin, sprinkler_pin)

while True:
    actuators.fan_on()
    time.sleep(3)
    actuators.heater_on()
    time.sleep(3)
    actuators.window_on()
    time.sleep(3)
    actuators.sprinkler_on()
    time.sleep(3)


adc = ADC(0, bits=12)
apin = adc.channel(pin="G14", attn=ADC.ATTN_11DB)
while True:
    print(apin())
    print(apin.voltage())
    time.sleep(5)