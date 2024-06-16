print("Running boot")

import binascii
from network import LoRa
import time

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
dev_eui = binascii.unhexlify('70B3D57ED0067A4B')
app_key = binascii.unhexlify('9ADEE127F73456E0EFA865FD65E7A537')
app_eui = binascii.unhexlify('0000000000000000')

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
print("Joining LoRa...")
while not lora.has_joined():
    time.sleep(2)
print('Joined!')

print("Boot Complete.")