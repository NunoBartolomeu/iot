print("Running main")

import sys
sys.path.append('./src')

import socket
import time
from machine import Pin, I2C, ADC # type: ignore
from dht import DHT
from Display import Display
from Message import Message
from Actuators import Actuators
from Limit import Limit

TEMP_LIMITS = Limit('T', 20, 30)
HUMI_LIMITS = Limit('H', 50, 60)

display = Display()
dht = DHT(Pin('G2', mode=Pin.OPEN_DRAIN),0)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(True)

fan_pin = Pin('G13', mode=Pin.OUT)
heater_pin = Pin('G14', mode=Pin.OUT)
window_pin = Pin('G25', mode=Pin.OUT)
sprinkler_pin = Pin('G15', mode=Pin.OUT)

actuators = Actuators(fan_pin, heater_pin, window_pin, sprinkler_pin)

SLEEP_TIME = 5

while True:
    #Get sensor data
    result = dht.read()

    if not result.is_valid():
        if result.error_code == 1:
            print("Error: %d, Bad physical connection!" % result.error_code)
        elif result.error_code == 2:
            print("Error: %d, Values out of sensor capacity!" % result.error_code)
        else:
            break
        SLEEP_TIME = 5#15

    else:
        message = Message(result.temperature, result.humidity)
        
        TEMP_LIMITS.check(message)
        HUMI_LIMITS.check(message)

        if not message.warning:
            SLEEP_TIME = 10#30
            print("No warnings.")
            actuators.all_off()
        else:
            SLEEP_TIME = 5#15
            if message.temp > TEMP_LIMITS.max:
                actuators.fan_on()
            if message.temp < TEMP_LIMITS.min:
                actuators.heater_on()
            if message.humi > HUMI_LIMITS.max:
                actuators.window_on()
            if message.humi < HUMI_LIMITS.min:
                actuators.sprinkler_on()
            

        display.showData(message, TEMP_LIMITS, HUMI_LIMITS)
        print(message)

        s.send(bytes([message.temp, message.humi]))
    time.sleep(SLEEP_TIME)
    
print("Left main loop!")

adc = ADC(0, bits=12)
apin = adc.channel(pin="G14", attn=ADC.ATTN_11DB)
while True:
    print(apin())
    print(apin.voltage())
    time.sleep(5)