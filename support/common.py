from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_Element(driver, by_locator):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_locator))

def get_Element_Text(driver, by_locator):
    return get_Element(driver, by_locator).text

def click_Element(driver, by_locator):
    return get_Element(driver, by_locator).click()

def type_Element(driver, by_locator, text):
    return get_Element(driver, by_locator).send_keys(text)

def is_Element_displayed(driver, by_locator):
    return get_Element(driver, by_locator).is_displayed()

def scroll_down_little(driver):
    driver.execute_script("window.scrollTo(0,100);")
