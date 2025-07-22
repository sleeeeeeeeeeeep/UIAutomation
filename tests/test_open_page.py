from utils.utils import find_and_click, verify_page_opened, move_mouse_to_window_bottom_center
import time

def test_tech_tree():
    """
    기술 발전표가 정상적으로 열리는지 테스트
    """
    time.sleep(3)  # 준비 시간
    assert find_and_click("templates/tech_button.png"), "기술 발전표 버튼을 찾지 못했습니다."
    move_mouse_to_window_bottom_center() # 툴팁이 화면을 가려서 마우스 강제이동
    assert verify_page_opened("templates/tech_page.png"), "기술 발전표 페이지가 열리지 않았습니다."


def test_civic_tree():
    """
    사회 제도표가 정상적으로 열리는지 테스트
    """
    time.sleep(3)  # 준비 시간
    assert find_and_click("templates/civ_button.png"), "사회 제도표 버튼을 찾지 못했습니다."
    move_mouse_to_window_bottom_center() # 툴팁이 화면을 가려서 마우스 강제이동
    assert verify_page_opened("templates/civ_page.png"), "사회 제도표 페이지가 열리지 않았습니다."

def test_person_page():
    """
    위인 페이지가 정상적으로 열리는지 테스트
    """
    time.sleep(3)  # 준비 시간
    assert find_and_click("templates/person_button.png"), "위인 버튼을 찾지 못했습니다."
    move_mouse_to_window_bottom_center() # 툴팁이 화면을 가려서 마우스 강제이동
    assert verify_page_opened("templates/person_page.png"), "위인 페이지가 열리지 않았습니다."

def test_weather_page():
    """
    위인 페이지가 정상적으로 열리는지 테스트
    """
    time.sleep(3)  # 준비 시간
    assert find_and_click("templates/weather_button.png"), "위인 버튼을 찾지 못했습니다."
    move_mouse_to_window_bottom_center() # 툴팁이 화면을 가려서 마우스 강제이동
    assert verify_page_opened("templates/weather_page.png"), "위인 페이지가 열리지 않았습니다."

def test_viceroy_page():
    """
    위인 페이지가 정상적으로 열리는지 테스트
    """
    time.sleep(3)  # 준비 시간
    assert find_and_click("templates/viceroy_button.png"), "총독 버튼을 찾지 못했습니다."
    #move_mouse_to_window_bottom_center() # 툴팁이 화면을 가려서 마우스 강제이동
    assert verify_page_opened("templates/viceroy_page.png"), "총독 페이지가 열리지 않았습니다."