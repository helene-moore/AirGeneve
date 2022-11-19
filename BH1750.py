import machine
from machine import I2C
import time
class BH1750():
    POWER_DOWN='\x00'
    POWER_ON='\x01'
    RESET='\x07'

    CONTINUOUS_LOW_RES_MODE = '\x13'
    CONTINUOUS_HIGH_RES_MODE_1 = '\x10'
    CONTINUOUS_HIGH_RES_MODE_2 = '\x11'
    ONE_TIME_HIGH_RES_MODE_1 = '\x20'
    ONE_TIME_HIGH_RES_MODE_2 = '\x21'
    ONE_TIME_LOW_RES_MODE = '\x23'
    def __init__(self, bus, addr=0x23):
        self.bus=bus
        self.addr=addr
        self.mode=0
        self.power_on()
        self.reset()
        self.contiHighRes()
    def power_down(self):
        self.bus.writeto(self.addr, self.POWER_DOWN)
    def power_on(self):
        self.bus.writeto(self.addr, self.POWER_ON)
    def reset(self):
        self.bus.writeto(self.addr, self.RESET)
    def contiHighRes(self):
        self.bus.writeto(self.addr, self.CONTINUOUS_HIGH_RES_MODE_2)
    def mesure(self):
        tab=self.bus.readfrom(self.addr, 2)
        return int.from_bytes(tab,'big')
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
print(i2c.scan())
sensor = BH1750(i2c)
while True:
    if sensor.mesure() > 500:
        print("Basse polution")
        print(sensor.mesure())
    elif sensor.mesure() > 35:
        print("Moyenne polution")
        print(sensor.mesure())
    else:
        print("Grosse polution")
        print(sensor.mesure())
    print('-------')
    time.sleep(3)
    #delay(1000)
