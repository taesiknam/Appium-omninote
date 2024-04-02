from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

def run_appium():
  options = AppiumOptions()
  options.load_capabilities({
      "platformName": "Android",
      "appium:deviceName": "Pixel_3a_API_34",
      "appium:app": "C:/android/TEST-OmniNotes-alphaDebug-6.3.2.apk",
      "appium:automationName": "UiAutomator2",
      "appium:autoGrantPermissions": True,
      "appium:ensureWebviewsHavePages": True,
      "appium:nativeWebScreenshot": True,
      "appium:newCommandTimeout": 3600,
      "appium:connectHardwareKeyboard": True
  })
  driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
  return driver

driver = run_appium

def find_elem_XPATH(driver, XPATH_value):
    find_elem_XPATH = driver.find_element(by=AppiumBy.XPATH, value=XPATH_value)
    return find_elem_XPATH

def find_elem_ID(driver, ID_value):
    find_elem_ID = driver.find_element(by=AppiumBy.ID, value=ID_value)
    return find_elem_ID