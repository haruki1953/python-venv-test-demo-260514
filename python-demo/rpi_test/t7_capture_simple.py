# t7_capture_simple.py
import asyncio


async def capture_to_memory_async(
    width: int = 640, height: int = 480, quality: int = 70, timeout_ms: int = 1
):
    # 构建命令
    cmd = [
        "rpicam-jpeg",
        "-o",
        "-",
        "-t",
        str(timeout_ms),
        "-n",
        "--width",
        str(width),
        "--height",
        str(height),
        "--quality",
        str(quality),
    ]

    # 创建子进程（异步）
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)

    # 等待拍照完成
    stdout, stderr = await proc.communicate()  # type: ignore
    # (variable) stdout: bytes

    # 返回 JPEG 二进制数据
    return stdout


async def main():
    img = await capture_to_memory_async(width=640, height=480, quality=70, timeout_ms=1)
    print("拍到的图片大小:", len(img), "字节")


asyncio.run(main())
