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
