from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import cv2
import tkinter as tk

from shifting import left_menu_to_x
from shifting import main_menu_to_x
from shifting import battle_general_to_x
from shifting import recognizing_current_window as recognize

from operation import change_equipment as ceq

import general_funcs as gf

import event_handle as eh


def oil_is_ready():  # 被用在收获里判断石油好了没
    return gf.check_color(219, 90, 60, 61, 60)


def money_is_ready():  # 被用在收获里判断钱好了没
    return gf.check_color(462, 110, 239, 182, 66)


def books_are_ready():  # 被用在收获里判断书好了没
    return gf.check_color(704, 110, 74, 82, 104)


def left_menu_to_collect_three_resources():  # 收三种资源
    if oil_is_ready() is True:
        pyautogui.leftClick(219, 90)  # 主界面左侧收获石油
    time.sleep(0.5)
    if money_is_ready() is True:
        pyautogui.leftClick(462, 110)  # 主界面左侧收获金币
    time.sleep(0.5)
    if books_are_ready() is True:
        pyautogui.leftClick(650, 100)  # 主界面左侧收获技能书
    time.sleep(0.5)


time.sleep(3)
while True:
    if gf.extract_word(1130, 870, 1414, 929) == "再次前往":
        pyautogui.leftClick(1314, 929)
    eh.full_storage_handle()
    time.sleep(1)
#
# gf.debug_show_mouse_in_window()
# print(recognize.judge_current())
# ceq.check_ultra_boss_status()
# ceq.change_accordingly(ceq.check_ultra_boss_status())
# time.sleep(5)
# eh.check_full_storage()
# eh.full_storage_handle()
# main_to_left_menu()
# left_menu_to_collect_three_resources()
# time.sleep(2)
# main_menu_to_x.main_to_battle_general()
# battle_general_to_x.battle_general_to_main_thread()
# main_thread_enter_12_4_without_selecting()
#
# after_entering_12_4_to_finish(False)
# main_to_left_menu()
# left_menu_to_missions()
# main_menu_to_x.main_to_left_menu()
# while 1:
#     print(recognize.judge_current())
