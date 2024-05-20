print("System booting up...")

import sys
sys.path.append('./src')
from Limit import Limit
import binascii
from network import LoRa
import time

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
dev_eui = binascii.unhexlify('70B3D57ED0067A4B')
app_key = binascii.unhexlify('9ADEE127F73456E0EFA865FD65E7A537')
app_eui = binascii.unhexlify('0000000000000000')

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print('Joined')


TEMP_LIMITS = Limit('T', 25, 20, 30)
HUMI_LIMITS = Limit('H', 55, 50, 60)

print(TEMP_LIMITS)
print(HUMI_LIMITS)

print("System booted up.")