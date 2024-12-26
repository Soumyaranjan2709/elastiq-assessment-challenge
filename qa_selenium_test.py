import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_functionality(driver):
    # Step 1: Navigate to Selenium Playground Table Search Demo
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    time.sleep(2)

    # Step 2: Locate the search box and search for "New York"
    Search_text = driver.find_element(By.XPATH, "//input[@type='search']")
    Search_text.send_keys("New York")
    time.sleep(2)

    # Step 3: Validate the search results
    rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    visible_rowCount = len(rows)

    # Step 4: Validate with the info text
    example_info = driver.find_element(By.ID, "example_info").text

    # Step 5: Simple validation
    assert (f"Showing 1 to {visible_rowCount} of {visible_rowCount}" in example_info), \
        "The info text does not match the visible rows count."
