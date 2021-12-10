# four LEDS numbered 1 to 4

import time  # time para delay
from pyb import LED  # classe led para acender leds


class ControlaLeds:
    @staticmethod
    def led_vermelho():
        led1 = LED(1)
        led1.toggle()
        time.sleep_ms(100)

    @staticmethod
    def led_verde():
        led2 = LED(2)
        led2.toggle()
        time.sleep_ms(100)

    @staticmethod
    def led_amarelo():
        led2 = LED(3)
        led2.toggle()
        time.sleep_ms(100)

    @staticmethod
    def led_azul():
        led2 = LED(4)
        led2.toggle()
        time.sleep_ms(100)


if __name__ == '__main__':  # devido aos recursos computacionais limitados 64KB de ram, não consegui implementar threads
    for n in range(1000):
        ControlaLeds.led_vermelho()
        ControlaLeds.led_verde()
        ControlaLeds.led_amarelo()
        ControlaLeds.led_azul()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     """ Outras implementações que fiz posteriormente:<br>
     import machine<br>

# The LED is connected to our virtual pin Y12<br>
y12 = machine.Pin('Y12')  # confere se há algo em Y12<br>
<br>
y12(0 if y12() else 1)  # se estiver desligado, liga<br>
<br>
<br>
# configurar uma saída<br>
from machine import Pin<br>
from time import sleep_ms<br>
<br>
y12 = Pin('Y12', Pin.OUT)  # configura o y12 como saída de led<br>
y12.on()<br>
sleep_ms(2000)<br>
y12.off()<br>
<br>
# push the USR button on the pyboard to flash the LEDs!<br>
# configuração de entrada<br>
<br>
import time<br>
from pyb import Switch, LED<br>
while True:<br>
    if Switch().value():  # switch é o botão, que troca o estado dependendo do valor, se nao preciona = 0, apaga<br>
        LED(1).on()<br>
        LED(2).on()<br>
    else:<br>
        LED(1).off()<br>
        LED(2).off()<br>
    time.sleep_ms(100)<br>"""

