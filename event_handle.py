from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import cv2

import general_funcs as gf


def check_full_storage():
    string = gf.extract_word(558, 715, 734, 782)
    return string == "整理"


def sr_ship_detected():
    string = gf.extract_word(793, 590, 1029, 646)
    return string == "是否确认"


def full_storage_handle():
    if check_full_storage():
        pyautogui.leftClick(724, 744)
        time.sleep(1)
        pyautogui.leftClick(1044, 964)
        time.sleep(0.5)
        pyautogui.leftClick(1433, 927)
        time.sleep(1)
        # 如果有紫船
        if sr_ship_detected():
            pyautogui.leftClick(1154, 722)
            time.sleep(1)
        pyautogui.leftClick(1433, 927)
        time.sleep(1)
        pyautogui.leftClick(1347, 796)
        time.sleep(1)
        pyautogui.leftClick(1144, 838)
        time.sleep(1)
        pyautogui.leftClick(1144, 838)
        time.sleep(1)
        pyautogui.leftClick(142, 109)
        time.sleep(2)
        if gf.check_color(1793, 838, 205, 123, 107):
            pyautogui.leftClick(1760, 814)

