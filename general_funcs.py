from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def extract_word(x1, y1, x2, y2):
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    gray = screenshot.convert('L')
    # screenshot.show()
    result = pytesseract.image_to_string(gray, lang='chi_sim')  # 使用中文简体和英文识别
    # print(result)
    screenshot.close()
    return result


def check_color(x, y, r, g, b):  # 检查位置为(x,y)的颜色是否为(r,g,b)
    screen = ImageGrab.grab()
    color = screen.getpixel((x, y))
    screen.close()
    if color[0] == r and color[1] == g and color[2] == b:
        return True
    else:
        return False
