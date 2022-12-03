from m5stack import *
import network
try:
    import usocket as socket
except:
    import socket
import boot
import BH1750
from machine import I2C


#Connection du m5stack au wifi

# Interface Wi-Fi "Station" (client)
sta_if = network.WLAN(network.STA_IF)
# Activation de l'interface
sta_if.active(True)
# Vérifier si l'interface est active
if sta_if.active():
    lcd.print("Interface Wi-Fi cliente active\n")
else:
    lcd.print("Interface Wi-Fi cliente inactive\n", color=0x00e8e4)
# connexion à un réseau existant

sta_if.connect('iot1', 'welcome2022')
#sta_if.connect('UPCA9385A1', 'Biloute444')


    
# Vérifier si l'interface est connectée
if sta_if.isconnected():
    lcd.print("Interface Wi-Fi cliente connectée\n")
else:
    lcd.print("Interface Wi-Fi cliente non connectée\n", color=0x00e8e4)



sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto("Test udp".encode('UTF-8'), ("192.168.10.123", 1235))


lcd.clear()
lcd.setCursor(0, 0)
lcd.setColor(lcd.WHITE)
#lcd.println("")
if sta_if.isconnected():
    lcd.print("Interface Wi-Fi cliente connectée\n")


    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
    print(i2c.scan())
    sensor = BH1750.BH1750(i2c)
    
    mesure = "LOW"

    while True:
        newMesure = ""
        if sensor.mesure() < 35:
            newMesure = "HIGH"
        elif sensor.mesure() < 500:
            newMesure = "MEDIUM"
        else:
            newMesure = "LOW"
        if(newMesure != mesure):
            print(newMesure)
            lcd.print(newMesure)
            sock.sendto(str(newMesure).encode('UTF-8'), ("192.168.10.123", 1235))

            mesure = newMesure
        #print(sensor.mesure())
            print('-------')
        time.sleep(6)
        

