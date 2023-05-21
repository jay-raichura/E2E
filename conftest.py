'''
E2E/conftest.py consists of all the common fixtures being used on TestCases/test_file.py
'''
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://demoqa.com/"  # URL to be used for demo site


@pytest.fixture(scope='function')
def driver():
    """
    This method will give the driver object
    :return: driver object
    """
    driver_obj = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver_obj


@pytest.fixture(scope='function')
@pytest.mark.usefixtures('driver')
def open_browser(driver):
    """
    This method will open the chrome browser.
    :param driver: driver object to launch chrome browser
    :return:
    """
    driver.get(URL)
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()


@pytest.fixture(scope='function')
@pytest.mark.usefixtures('driver')
def action_chain(driver):
    """
    This method will return action chain object
    :param driver: driver object
    :return:
    """
    action_chain_obj = ActionChains(driver)
    return action_chain_obj
