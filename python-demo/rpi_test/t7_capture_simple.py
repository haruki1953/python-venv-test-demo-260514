# t7_capture_simple.py
import asyncio


async def capture_to_memory_async(
    width: int = 640, height: int = 480, quality: int = 70, timeout_ms: int = 1
):
    # 构建命令列表，每个元素都是命令行中的一个参数
    # 例如：rpicam-jpeg -o - -t 1 -n --width 640 --height 480 --quality 70
    cmd = [
        "rpicam-jpeg",  # 调用树莓派摄像头的拍照程序
        "-o",
        "-",  # 输出到标准输出（stdout），不写入文件
        "-t",
        str(timeout_ms),  # 拍照前等待的时间（毫秒）
        "-n",  # 不显示预览窗口
        "--width",
        str(width),  # 设置图片宽度
        "--height",
        str(height),  # 设置图片高度
        "--quality",
        str(quality),  # JPEG 压缩质量（0-100）
    ]

    # 创建一个异步子进程来执行拍照命令
    # stdout=PIPE 表示我们要读取拍到的 JPEG 二进制数据
    # stderr=DEVNULL 表示忽略 libcamera 的日志输出
    proc = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL
    )

    # 等待子进程执行完毕，并一次性读取它的输出
    # stdout 是 JPEG 图片的二进制内容
    # stderr 被忽略（因为我们设置为 DEVNULL）
    stdout, stderr = await proc.communicate()  # type: ignore

    # 返回 JPEG 二进制数据
    return stdout


async def main():
    # 调用拍照函数，得到 JPEG 图片的二进制内容
    img = await capture_to_memory_async(width=640, height=480, quality=70, timeout_ms=1)

    # 将二进制内容写入文件 testaaa.jpg
    # "wb" 表示以二进制方式写入文件
    with open("testaaa.jpg", "wb") as f:
        f.write(img)

    # 打印保存成功的信息
    print("已保存到 testaaa.jpg，大小:", len(img), "字节")


# 运行异步主函数
asyncio.run(main())
