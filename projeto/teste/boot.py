print("System booting up...")

import sys
sys.path.append('./src')
from Limit import Limit

TEMP_LIMITS = Limit('T', 25, 20, 30)
HUMI_LIMITS = Limit('H', 55, 50, 60)

print(TEMP_LIMITS)
print(HUMI_LIMITS)

print("System booted up.")