# t6_mh_sensor_read.py
import asyncio
from gpiozero import DigitalInputDevice  # type: ignore


async def main():

    rain = DigitalInputDevice(12)  # 雨滴检测模块 DO
    light = DigitalInputDevice(17)  # 光敏模块 DO
    press_head = DigitalInputDevice(27)  # 压力检测 床头 DO
    press_foot = DigitalInputDevice(22)  # 压力检测 床尾 DO

    while True:
        print("---- 传感器状态 ----")

        print("雨滴检测：", "有雨" if rain.value == 0 else "无雨")
        print("光敏检测：", "亮" if light.value == 0 else "暗")
        print("床头压力：", "有压" if press_head.value == 0 else "无压")
        print("床尾压力：", "有压" if press_foot.value == 0 else "无压")

        print("-------------------\n")

        await asyncio.sleep(1)


asyncio.run(main())
