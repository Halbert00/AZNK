import time
import pyautogui


def main_to_left_menu():
    pyautogui.leftClick(100, 225)  # 主界面调出左边栏
    time.sleep(0.5)


def main_to_battle_general():  # 主界面点击出击
    pyautogui.leftClick(1556, 548)
    time.sleep(0.5)
