from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import cv2

import general_funcs as gf


def judge_current():
    if gf.extract_word(1227, 546, 1400, 620) == "编队":  # 主界面
        return 0
    if gf.extract_word(587, 404, 721, 454) == "前往":  # 主界面侧边栏
        return 1
    if gf.extract_word(1210, 264, 1390, 313) == "贸易许可证":  # 商店总界面
        return 2
    if gf.extract_word(223, 45, 390, 99) == "换装商店":  # 皮肤界面
        return 3
    if gf.extract_word(223, 45, 390, 99) == "钻石购买":  # 钻石商店
        return 4
    if gf.extract_word(223, 45, 327, 99) == "商店":  # 补给商店
        return 5
    if gf.extract_word(1616, 747, 1770, 796) == "先锋舰队" or gf.extract_word(1616, 747, 1770, 796) == "潜艇舰队":  # 编队界面
        return 6
    if gf.extract_word(223, 45, 327, 99) == "出击":  # 出击界面
        if gf.extract_word(172, 931, 266, 976) == "普通":  # 主线/活动困难
            return 7
        if gf.extract_word(172, 931, 266, 976) == "困难":  # 主线/活动普通
            return 8
        return 9
