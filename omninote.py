from appium.webdriver.common.appiumby import AppiumBy
import pytest, time

# For W3C actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import run_appium, find_elem_XPATH,find_elem_ID #appium 실행
from XPATH import FAB_XPATH, TN_tooltip_XPATH,TN_Button_XPATH, TN_Back_XPATH, TN_Body_ID,TN_Title_ID, drawer_body_ID,drawer_title_ID

driver = run_appium()

@pytest.fixture()
def Open_APP():
    # Webdriver wait 최대:10초
    wait = WebDriverWait(driver, 10)
    
    # 예제: 앱이 실행되고 "Notes" 텍스트가 나타날 때까지 대기합니다.
    home_element = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Notes']")))
    return home_element

@pytest.fixture()
def Open_FAB():
    #FAB 요소 찾아서 선택      
    find_elem_XPATH(driver,FAB_XPATH).click()
    wait = WebDriverWait(driver, 10)
    text_note = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, TN_tooltip_XPATH)))
    return text_note

@pytest.fixture()
def Open_Text_note():
    #FAB 요소 찾아서 선택      
    find_elem_XPATH(driver,TN_Button_XPATH).click()
    wait = WebDriverWait(driver, 10)
    Title = wait.until(EC.visibility_of_element_located((AppiumBy.ID, TN_Title_ID)))
    return Title

@pytest.fixture()
def Write_Title():
    # Title 요소 찾기
    Title = find_elem_ID(driver,TN_Title_ID)
    # Title Hello world 입력
    Title.send_keys("Hello World")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((AppiumBy.ID, TN_Title_ID), "Hello World"))
    return Title

@pytest.fixture()
def Write_Body():
    # Title 요소 찾기
    BODY = find_elem_ID(driver,TN_Body_ID)
    # Title Hello world 입력
    BODY.click()
    BODY.send_keys("Hello World")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((AppiumBy.ID, TN_Body_ID), "Hello World"))
    return BODY

@pytest.fixture()
def Click_back():
    find_elem_XPATH(driver, TN_Back_XPATH).click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((AppiumBy.ID, drawer_title_ID)))
    result_title = find_elem_ID(driver,drawer_title_ID).text
    result_body = find_elem_ID(driver,drawer_body_ID).text
    return {
        'result_title' : result_title,
        'result_body' : result_body
        }