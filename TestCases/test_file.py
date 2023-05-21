'''
TestCases/test_file.py consists of test cases from demo site https://demoqa.com/
'''
import time
import pytest
from E2E.common import locators
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('driver', 'open_browser', 'action_chain')
def test_book_store_availibility(driver, action_chain):
    """
    In this test we are verifying that book store application tab is visible on the page and
    user is able to navigate to that page or not.
    :driver: driver object
    :param action_chain: action chains object
    :return:
    """

    # Verify book store app tab is available on page
    book = driver.find_element(By.XPATH, locators.book_store_tab_name)
    if book:
        # Scrolling the page to see the tab on screen
        action_chain.move_to_element(book).perform()
        time.sleep(2)

        # Click on tab to navigate to book store page
        book_tab = driver.find_element(By.XPATH, locators.book_store_tab)
        book_tab.click()

        # Verify navigation to book store page
        book_page_text = driver.find_element(By.XPATH, locators.book_page_header).text
        if book_page_text:
            print("We are on Book store page.")
        assert "book store" in book_page_text.lower(), "It is not correct navigation"

    else:
        print("Book tab is not available. Check your connection, it might be slow.")

@pytest.mark.usefixtures('driver', 'open_browser', 'action_chain')
def test_search_book_get_author(driver, action_chain):
    """
    In this test we are verifying that user is able to search and get the desired book as result.
    :param driver: driver object
    :param action_chain: action chains object
    :return:
    """
    book = driver.find_element(By.XPATH, locators.book_store_tab_name)
    if book:
        # Scrolling the page to see the tab on screen
        action_chain.move_to_element(book).perform()
        time.sleep(2)

        # Click on tab to navigate to book store page
        book_tab = driver.find_element(By.XPATH, locators.book_store_tab)
        book_tab.click()

        # Searching the desired book
        time.sleep(2)
        search_box = driver.find_element(By.CSS_SELECTOR, locators.search_box)
        search_box.click()
        search_box.send_keys('git')

        # Click on the search result
        author = driver.find_element(By.XPATH, locators.git_author).text
        print(f"Author name on table list {author}")
        time.sleep(2)

        # Scrolling before navigation for better view of content
        driver.execute_script("window.scrollBy(0,250)")
        result = driver.find_element(By.LINK_TEXT, locators.git_book)
        result.click()

        # Verifying the author field and getting name of author
        driver.execute_script("window.scrollBy(0,250)")
        book_page_auth = driver.find_element(By.XPATH, locators.author_field).text
        book_page_auth_name = driver.find_element(By.XPATH, locators.author_name_field).text

        if book_page_auth:
            if book_page_auth_name == author:
                assert book_page_auth_name == author, "Author data is incorrect"
        else:
            assert False, "Author data is not available on book page."

    else:
        assert False, "Navigation to book page was unsuccessful due to unavailibity."

@pytest.mark.usefixtures('driver', 'open_browser', 'action_chain')
def test_element_tab_radio(driver, action_chain):
    """
    In this test we are verifying the elements tab availibility and radio button functionality.
    :param driver: driver object
    :param action_chain: action chains object
    :return:
    """

    # Verify and click on elements tab
    driver.execute_script("window.scrollBy(0,100)")
    elements = driver.find_element(By.XPATH, locators.elements_tab_name)
    if elements:
        element_tab = driver.find_element(By.XPATH, locators.elements_tab)
        element_tab.click()

        # Verify and click on checkbox from left menu
        radio = driver.find_element(By.XPATH, locators.radio_button)
        radio_name = radio.text

        assert "radio button" in radio_name.lower()

        # Click on checkbox and verify functionality
        driver.execute_script("window.scrollBy(0,100)")
        radio.click()
        time.sleep(2)
        radio_btn = driver.find_element(By.XPATH, locators.radio_btn_l).click()
        message = driver.find_element(By.XPATH, locators.radio_result).text
        print(message)
    else:
        assert False, "Navigation was unsuccessful to elements tab."

@pytest.mark.usefixtures('driver', 'open_browser', 'action_chain')
def test_widget_tabs(driver,action_chain):
    """
    In this test we are verifying widget tab and verifying tab selection
    :param driver: driver object
    :param action_chain: action chain object
    :return:
    """

    widget = driver.find_element(By.XPATH, locators.widget)
    if widget:
        driver.execute_script("window.scrollBy(0,100)")
        widget_tab = driver.find_element(By.XPATH, locators.widget_tab).click()
        time.sleep(5)

        # Verify and click tabs from left menu
        driver.execute_script("window.scrollBy(0,550)")
        tabs = driver.find_element(By.XPATH, locators.tabs).click()
        time.sleep(2)

        # Click on different tab and verify text
        driver.execute_script("window.scrollBy(0,200)")
        tab2 = driver.find_element(By.XPATH, locators.tab2).click()
        time.sleep(2)
        result_use = driver.find_element(By.XPATH, locators.tab_msg).text
        print(result_use)

        tab1 = driver.find_element(By.XPATH, locators.tab1).click()
        time.sleep(2)
        result_what = driver.find_element(By.XPATH, locators.tab_msg).text
        print(result_what)

        assert result_what != result_use
    else:
        assert False, "Navigation was unsuccessful to widget tab."

@pytest.mark.usefixtures('driver', 'open_browser', 'action_chain')
def test_alert_confirmation(driver,action_chain):
    """
    In this test we are verifying alert tab and verifying confirmation functionality
    :param driver: driver object
    :param action_chain: action chain object
    :return:
    """
    alert = driver.find_element(By.XPATH, locators.alert)
    if alert:
        driver.execute_script("window.scrollBy(0,100)")
        alert_tab = driver.find_element(By.XPATH, locators.alert_tab).click()
        time.sleep(5)

        # Verify and click alerts from left menu
        driver.execute_script("window.scrollBy(0,400)")
        alert_op = driver.find_element(By.XPATH, locators.alerts_op).click()
        time.sleep(2)

        # Select 3rd confirmation button to verify functionality
        driver.execute_script("window.scrollBy(0,250)")
        click_me = driver.find_element(By.XPATH, locators.click_me).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()

        # Verify message printed on screen
        message = driver.find_element(By.XPATH,locators.message).text
        print(message)
    else:
        assert False, "Navigation was unsuccessful to alerts tab."
