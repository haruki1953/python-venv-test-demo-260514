# test\t1_led_control.py
import asyncio
from gpiozero import LED  # type: ignore


async def main():

    led_run = LED(16)
    led_net = LED(20)
    led_auto = LED(21)

    while True:
        led_run.on()
        led_net.off()
        led_auto.on()
        await asyncio.sleep(1)

        led_run.off()
        led_net.on()
        led_auto.off()
        await asyncio.sleep(1)


asyncio.run(main())
