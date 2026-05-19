# test/t2_button_test.py
import asyncio
from gpiozero import Button  # type: ignore


async def main():
    # 定义按键（你的接线：GPIO --- 按键 --- GND）
    btn_up = Button(6)  # 亮度增加
    btn_down = Button(13)  # 亮度减少
    btn_mode = Button(19)  # 模式切换
    btn_call = Button(26)  # 呼叫按键

    print("按键测试启动，按下任意按键试试…")

    # 事件绑定（按下触发）
    btn_up.when_pressed = lambda: print("亮度增加键 按下")
    btn_down.when_pressed = lambda: print("亮度减少键 按下")
    btn_mode.when_pressed = lambda: print("模式切换键 按下")
    btn_call.when_pressed = lambda: print("呼叫键 按下")

    # asyncio 主循环保持运行
    while True:
        await asyncio.sleep(0.1)


asyncio.run(main())
