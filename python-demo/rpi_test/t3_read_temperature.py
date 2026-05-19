import asyncio
from w1thermsensor import W1ThermSensor  # type: ignore


async def main():
    sensor = W1ThermSensor()

    while True:
        try:
            temp = sensor.get_temperature()
            print(f"温度: {temp:.1f} °C")
        except Exception as e:
            print(f"读取温度失败: {e}")

        await asyncio.sleep(1)


asyncio.run(main())
