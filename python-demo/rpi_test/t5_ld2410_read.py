# t5_ld2410_read.py
import asyncio
from gpiozero import DigitalInputDevice  # type: ignore


async def main():

    # LD2410C OUT → GPIO5
    sensor = DigitalInputDevice(5)

    while True:
        if sensor.value == 1:
            print("有人")
        else:
            print("无人")

        await asyncio.sleep(1)


asyncio.run(main())
