from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import pytesseract
import cv2

import general_funcs as gf


def check_full_storage():
    string = gf.extract_word(558, 715, 734, 782)
    if len(string) == 0:
        return False
    elif string[0] == '整' and string[1] == '理':
        return True
    else:
        assert 0


def can_retire():
    string = gf.extract_word(284, 915, 378, 963)
    if len(string) == 0:
        return False
    elif string[0] == '可' and string[1] == '获' and string[2] == '得':
        return True


def full_storage_handle():
    if check_full_storage():
        pyautogui.leftClick(724, 744)
        time.sleep(1)
        while True:
            pyautogui.leftClick(1044, 964)
            time.sleep(0.5)
            if can_retire() is False:
                break
            pyautogui.leftClick(1433, 927)
            time.sleep(1)
            pyautogui.leftClick(1433, 927)
            time.sleep(1)
            pyautogui.leftClick(1347, 796)
            time.sleep(1)
            pyautogui.leftClick(1144, 838)
            time.sleep(1)
            pyautogui.leftClick(1144, 838)
            time.sleep(1)


def first_is_purple():
    if gf.check_color(438, 395, 209, 210, 226) and gf.check_color(449, 401, 214, 211, 231):
        return True


def second_is_gold():
    if gf.check_color(702, 402, 206, 211, 231) and gf.check_color(713, 408, 214, 215, 238):
        return True


def third_is_energy():  # 暂时是蓝色
    if gf.check_color(957, 430, 66, 64, 57) and gf.check_color(968, 433, 66, 65, 57):
        return True


def fourth_is_energy():  # 暂时是紫色
    if gf.check_color(1217, 431, 72, 69, 66) and gf.check_color(1215, 430, 74, 69, 66):
        return True
