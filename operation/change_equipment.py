from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import cv2

import general_funcs as gf


def check_ultra_boss_status():
    if gf.extract_word(1505, 922, 1704, 977) == "开始战斗":
        if gf.extract_word(228, 474, 330, 500)[0] == '轻':
            return 1
        elif gf.extract_word(228, 474, 330, 500)[0] == '中':
            return 2
        elif gf.extract_word(228, 474, 330, 500)[0] == '重':
            return 3
    return 0


def change_accordingly(op):  # 暂时实现更换预设装备的功能
    pyautogui.leftClick(131, 105)
    time.sleep(0.5)
    pyautogui.leftClick(409, 944)
    time.sleep(0.5)
    pyautogui.leftClick(362, 850)
    time.sleep(0.5)
    pyautogui.mouseDown(x=130, y=270)
    pyautogui.sleep(2)
    pyautogui.mouseUp()

    pyautogui.leftClick(1708, 173)
    time.sleep(0.5)
    if op > 1:
        pyautogui.leftClick(1740, 439)
    else:
        pyautogui.leftClick(1740, 586)
    time.sleep(0.5)
    pyautogui.moveTo(600, 554)
    pyautogui.dragTo(300, 554, 0.7, button='left')
    time.sleep(0.5)
    pyautogui.leftClick(1708, 173)
    time.sleep(0.5)
    if op > 1:
        pyautogui.leftClick(1740, 439)
    else:
        pyautogui.leftClick(1740, 586)
    time.sleep(0.5)
    pyautogui.moveTo(600, 554)
    pyautogui.dragTo(300, 554, 0.7, button='left')
    time.sleep(0.5)
    pyautogui.leftClick(1708, 173)
    time.sleep(0.5)
    if op > 1:
        pyautogui.leftClick(1740, 439)
    else:
        pyautogui.leftClick(1740, 586)
    pyautogui.leftClick(131, 105)
    time.sleep(0.5)
