import pydirectinput as pdi
import pygetwindow as gw
import cv2
import numpy as np
import time
from PIL import ImageGrab

def find_and_click(template_path: str, threshold=0.8, timeout=10):
    """
    화면에서 template_path를 찾아 클릭
    """
    start_time = time.time()
    template = cv2.imread(template_path, 0)
    if template is None:
        raise FileNotFoundError(f"이미지 없음: {template_path}")

    w, h = template.shape[::-1]

    # 설정한 시간동안 이미지 탐색하고 이미지 있으면 클릭
    while time.time() - start_time < timeout:
        screenshot = ImageGrab.grab()
        screen_np = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            x, y = pt[0] + w // 2, pt[1] + h // 2
            pdi.moveTo(x, y)
            time.sleep(0.1)
            pdi.click()
            print(f"클릭 좌표 {template_path}: {x},{y}")
            return True

    print(f"이미지 찾기 실패 {template_path}: {timeout} 초")
    return False

def verify_page_opened(template_path: str, threshold=0.8, timeout=5):
    """
    페이지가 열렸는지 확인
    """
    start_time = time.time()
    template = cv2.imread(template_path, 0)

    # 설정한 시간동안 이미지 탐색
    while time.time() - start_time < timeout:
        screenshot = ImageGrab.grab()
        screen_np = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        if (res >= threshold).any():
            print(f"pass: {template_path} 열림")
            return True

    print(f"fail: {template_path} 열리지 않음")
    return False

def activate_game_window(window_title_keyword="Sid Meier's Civilization VI (DX12)"):
    """
    게임 창 활성화
    """

    windows = gw.getWindowsWithTitle(window_title_keyword)
    if not windows:
        print(f"게임 창 못 찾음: {window_title_keyword}")
        return False
    
    win = windows[0]

    # 비활성화일 때
    if not win.isActive:
        win.activate()
        time.sleep(1)  # 활성화될 시간 조금 주기

    # 최소화일 때
    if win.isMinimized:
        win.restore()
        time.sleep(1)

    print(f"게임 창 활성화: {win.title}")
    return True

def get_active_window_rect():
    """
    해상도 반환
    """

    win = gw.getActiveWindow()
    if win is None:
        raise Exception("활성 창을 못 찾음")
    return win.left, win.top, win.width, win.height

def move_mouse_to_window_bottom_center():
    """
    마우스 창 중간 아래로 이동
    """

    left, top, width, height = get_active_window_rect()
    x = left + width // 2
    y = top + height - 1
    pdi.moveTo(x, y)