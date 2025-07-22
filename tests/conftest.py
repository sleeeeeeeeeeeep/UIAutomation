import pytest
import sys
import os
import datetime
from PIL import ImageGrab

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

import pytest
from utils.utils import activate_game_window, move_mouse_to_window_bottom_center

@pytest.fixture(scope="function", autouse=True)
def setup_game_window():
    assert activate_game_window(), "게임 창을 활성화할 수 없습니다."

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 테스트 실행 결과 가져오기
    outcome = yield
    rep = outcome.get_result()

    # 실패한 테스트 함수의 'call' 단계에서만 동작
    if rep.when == "call" and rep.failed:
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{item.name}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, file_name)

        # 화면 전체 스크린샷 저장
        img = ImageGrab.grab()
        img.save(filepath)

        # pytest-html 플러그인에 스크린샷 첨부
        if "pytest_html" in item.config.pluginmanager.list_name_plugin():
            extra = getattr(rep, "extra", [])
            html = f'<div><img src="{filepath}" alt="screenshot" style="width:600px;"></div>'
            # pytest-html 3.x 이상에서 extras 사용법
            from pytest_html import extras
            extra.append(extras.html(html))
            rep.extra = extra