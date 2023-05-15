from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import pytesseract
import cv2

from shifting import left_menu_to_x
from shifting import main_menu_to_x
from shifting import battle_general_to_x


def battle_finish_check():  # 检查战斗是否终止
    if check_color(970, 555, 255, 255, 255) and check_color(1015, 549, 255, 255, 255):
        if check_color(998, 304, 226, 171, 80) and check_color(1059, 555, 255, 255, 255):
            if check_color(991, 384, 230, 211, 107) and check_color(996, 459, 239, 243, 148):
                return True
    return False


def whole_12_4_finished():  # 检查12-4整体是否结束
    if check_color(609, 175, 255, 255, 255) and check_color(773, 159, 255, 255, 255):
        if check_color(694, 169, 255, 255, 255) and check_color(722, 171, 255, 255, 255):
            if check_color(780, 175, 255, 255, 255) and check_color(853, 162, 82, 113, 181):
                return True
    return False


def main_thread_enter_12_4_without_selecting():  # 主线不选关直接打12-4
    # 选了12-4
    pyautogui.leftClick(1459, 796)
    time.sleep(0.5)
    # 自律勾上
    if check_color(1265, 863, 156, 235, 82) is False:
        pyautogui.leftClick(1265, 863)
    # 立即出击
    pyautogui.leftClick(1334, 749)
    time.sleep(0.2)
    # 取消潜艇
    pyautogui.leftClick(1636, 690)
    # 立即出击
    pyautogui.leftClick(1536, 889)
    time.sleep(1)


def after_entering_12_4_to_finish(op):  # 进入12—4以后一直打到结束
    # 自律取消掉
    pyautogui.leftClick(1753, 819)
    time.sleep(2)
    # 让自律一个敌人然后取消
    pyautogui.leftClick(1753, 819)
    time.sleep(0.05)
    pyautogui.leftClick(1753, 819)
    while battle_finish_check() is False:
        time.sleep(1)
    pyautogui.leftClick(1548, 951)
    time.sleep(0.5)
    pyautogui.leftClick(1548, 951)
    time.sleep(2)
    pyautogui.leftClick(1548, 951)
    time.sleep(2)
    pyautogui.moveTo(259, 116)
    pyautogui.dragTo(1719, 879, 0.2, button='left')
    pyautogui.moveTo(259, 116)
    pyautogui.dragTo(1719, 879, 0.2, button='left')
    pyautogui.moveTo(259, 116)
    pyautogui.dragTo(1719, 879, 0.2, button='left')
    pyautogui.moveTo(1803, 527)
    pyautogui.dragTo(600, 527, 0.2, button='left')
    # 补充弹药
    pyautogui.leftClick(1410, 824)
    # 继续自律寻敌
    pyautogui.leftClick(1753, 819)
    #
    while whole_12_4_finished() is False:
        time.sleep(1)
    if op is True:
        pyautogui.leftClick(1222, 877)
    time.sleep(2)


def check_color(x, y, r, g, b):  # 检查位置为(x,y)的颜色是否为(r,g,b)
    screen = ImageGrab.grab()
    color = screen.getpixel((x, y))
    screen.close()
    if color[0] == r and color[1] == g and color[2] == b:
        return True
    else:
        return False


def oil_is_ready():  # 被用在收获里判断石油好了没
    return check_color(219, 90, 60, 61, 60)


def money_is_ready():  # 被用在收获里判断钱好了没
    return check_color(462, 110, 239, 182, 66)


def books_are_ready():  # 被用在收获里判断书好了没
    return check_color(704, 110, 74, 82, 104)


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


def debug_print_mouse(a):  # 用于测鼠标位置，输入的a用于表示测量间隔
    while 1:
        x, y = pyautogui.position()
        print("x:", x, "y:", y)
        screen = ImageGrab.grab()
        color = screen.getpixel((x, y))
        screen.close()
        print("r:", color[0], "g:", color[1], "b:", color[2])
        time.sleep(a)


# time.sleep(5)
# main_to_left_menu()
# left_menu_to_collect_three_resources()
# time.sleep(2)
# main_to_battle_general()
# battle_general_to_main_thread()
# main_thread_enter_12_4_without_selecting()

# after_entering_12_4_to_finish(False)
# main_to_left_menu()
# left_menu_to_missions()
# main_menu_to_x.main_to_left_menu()


pytesseract.pytesseract.tesseract_cmd = 'D:/Tesseract/tesseract.exe'

pic = cv2.imread("D:/img/1.png")
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
result = pytesseract.image_to_string(gray, lang='chi_sim', config='--psm 6')
print("1 " + result)

pic = cv2.imread("D:/img/2.png")
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
result = pytesseract.image_to_string(gray, lang='chi_sim', config='--psm 6')
print("2 " + result)

pic = cv2.imread("D:/img/3.png")
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
result = pytesseract.image_to_string(gray, lang='chi_sim', config='--psm 6')
print("3 " + result)


# debug_print_mouse(1)
