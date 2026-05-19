# t7_capture_simple.py
import asyncio
from picamera import PiCamera


async def capture_image():
    camera = PiCamera()

    # 4:3 分辨率，接近 400x400
    camera.resolution = (400, 300)

    # 异步预热摄像头
    await asyncio.sleep(2)

    out_file = "capture_400x300_q70.jpg"

    camera.capture(out_file, format="jpeg", quality=70)
    camera.close()

    print(f"Saved: {out_file}")


asyncio.run(capture_image())
