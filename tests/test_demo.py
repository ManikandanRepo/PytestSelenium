import time

from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By
from support.common import *


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    return driver
    driver.close()
    driver.quit()

def test_open_url(driver):
    #driver.get("http://dbankdemo.com/bank/login")
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    assert "DEMOQA" == driver.title

    #assert "Digital Bank" == driver.title

def test_Click_ElementSection(driver):
    # type_Element(driver, (By.ID, "username"), 'jsmith@demo.io')
    # type_Element(driver, (By.ID, "password"), 'Demo123!')
    # click_Element(driver, (By.ID, "submit"))
    #type_Element(driver, (By.ID, "email"), 'manijayam35@gmail.com')
    #type_Element(driver, (By.ID, "passwd"), 'Admin@123')
    time.sleep(2)
    scroll_down_little(driver)
    click_Element(driver, (By.XPATH, "//*[text()='Elements']"))
    time.sleep(5)
    assert "https://demoqa.com/elements" == driver.current_url


def test_Validate_TextBox_Functionality(driver):
    #click_Element(driver, (By.ID, "aboutLink"))
    click_Element(driver, (By.XPATH, "//*[text()='Text Box']"))
    assert is_Element_displayed(driver, (By.CSS_SELECTOR,"#userName-label"))

    #assert "CUSTOMER SERVICE - CONTACT US" in get_Element_Text(driver , (By.XPATH, "//*[@id='center_column']/h1"))
    # assert "2.1.0.11" in get_Element_Text(driver, (By.CLASS_NAME, "modal-body"))
