import pytest
import sys
import os
import datetime
from PIL import ImageGrab

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

import pytest
from action.utils import activate_game_window, move_mouse_to_window_bottom_center

@pytest.fixture(scope="function", autouse=True) # 모든 테스트 동작 전에 실행
def setup_game_window():
    assert activate_game_window(), "게임 창을 활성화할 수 없습니다."

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    # 테스트 실행 결과 가져오기
    outcome = yield
    rep = outcome.get_result()

    # 테스트 중 실패했을 때 스크린샷 찍어서 저장
    if rep.when == "call" and rep.failed:
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{item.name}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, file_name)

        # 화면 전체 스크린샷 저장
        img = ImageGrab.grab()
        img.save(filepath)
