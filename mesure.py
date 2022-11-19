from m5stack import lcd
from m5stack import *

lcd.print('Mesure en cours...')
speaker.volume(2)
noire=66
speaker.tone(freq=261, duration=noire) # C
delay(noire)
lcd.image(100, 100, file="C:/Users/helen/OneDrive/Bureau/mesure.png", scale=0, type=lcd.JPG)

#image0 = M5Img("C:/Users/helen/OneDrive/Documents/UNI/2022-2023/Automne 2022/ENTREPRISE CONNECTÉE/Projet/mesure.png", x=0, y=0, parent=None)