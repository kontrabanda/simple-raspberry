from gpiozero import LED
from time import sleep
import asyncio

async def light_test():
    led21 = LED(21)
    led16 = LED(16)
    led20 = LED(20)

    light(led21)
    light(led20)
    light(led16)


def light(led):
    led.on()
    sleep(5)
    led.off()
