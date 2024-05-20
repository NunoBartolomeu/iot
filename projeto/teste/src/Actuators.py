class Actuators:
    def __init__(self, fan_pin, heater_pin, window_pin, sprinkler_pin):
        self.fan_pin = fan_pin
        self.heater_pin = heater_pin
        self.window_pin = window_pin
        self.sprinkler_pin = sprinkler_pin
    
    def fan_on(self):
        self.fan_pin.value(1)
        self.heater_off()
    def fan_off(self):
        self.fan_pin.value(0)

    def heater_on(self):
        self.heater_pin.value(1)
        self.fan_off()  
    def heater_off(self):
        self.heater_pin.value(0)

    def window_on(self):
        self.window_pin.value(1)
        self.sprinkler_off()
    def window_off(self):
        self.window_pin.value(0)

    def sprinkler_on(self):
        self.sprinkler_pin.value(1)
        self.window_off()
    def sprinkler_off(self):
        self.sprinkler_pin.value(0)
        