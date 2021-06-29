from selenium import webdriver
import pytest
import allure

@pytest.fixture()
def test_setup():
     global driver
     driver = webdriver.Chrome("/Users/caglarfindikli/PycharmProjects/DemoNozzle/drivers/chromedriver")
     driver.maximize_window()
     yield
     driver.close()

def test_login(test_setup):
    driver.get("https://demo.nozzlesoft.com/")
    driver.find_element_by_id("Email").send_keys("jfindikli@gmail.com")
    driver.find_element_by_id("Password").send_keys("DL6U9fB?4")
    driver.find_element_by_id("btnLogin").click()

    assert driver.find_element_by_css_selector("#kt_header > div > div.topbar > div:nth-child(3) > div.topbar-item > div > span.text-dark-50.font-weight-bolder.font-size-base.d-none.d-md-inline.mr-3").is_displayed() is True
