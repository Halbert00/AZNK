from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import cv2
import numpy as np
import tkinter as tk
from cnocr import CnOcr


# 这个函数用于从屏幕的某一个部分提取出相应文字，四个值分别是截取区域的左上角坐标，和右下角坐标
def extract_word(x1, y1, x2, y2):
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    ocr = CnOcr()
    res = ocr.ocr(screenshot)
    text = "ori\n"
    if len(res) > 0:
        text = res[0]['text']
        print(text)
    return text


def check_color(x, y, r, g, b):  # 检查位置为(x,y)的颜色是否为(r,g,b)
    screen = ImageGrab.grab()
    color = screen.getpixel((x, y))
    screen.close()
    if color[0] == r and color[1] == g and color[2] == b:
        return True
    else:
        return False


# 接下来的部分是用于调试的，调用debug_show_mouse_in_window函数可以在左上角创建一个窗口，显示实时的鼠标坐标，可以辅助点击，截图的坐标的选取
def debug_show_mouse_in_window():
    def update_mouse_position():
        x, y = pyautogui.position()
        screen = ImageGrab.grab()
        color = screen.getpixel((x, y))
        position_label.config(text=f"Mouse Position: ({x}, {y})\n Color:({color[0]},{color[1]},{color[2]})")
        position_label.after(100, update_mouse_position)
    # 创建窗口
    window = tk.Tk()
    window.title("Mouse Position Tracker")
    window.attributes('-topmost', True)
    window.geometry("200x50+0+0")
    # 创建标签，用于显示鼠标位置
    position_label = tk.Label(window, text="Mouse Position: ")
    position_label.pack()

    # 更新鼠标位置
    update_mouse_position()

    # 运行窗口主循环
    window.mainloop()
