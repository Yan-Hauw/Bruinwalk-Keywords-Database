# libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def locate_course(browser, course_name):

    # Find and then type course name into the search box

    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(
            (
                By.XPATH,
                "//form[@class='search-form']/div[1]/input[@class='autocomplete']",
            )
        )
    )

    search_box = browser.find_element(
        By.XPATH, "//form[@class='search-form']/div[1]/input[@class='autocomplete']"
    )

    js = 'arguments[0].setAttribute("value", "' + course_name + '")'
    browser.execute_script(js, search_box)

    # Find and then click the search icon

    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//form[@class='search-form']/div[1]/i[@class='icon-search']")
        )
    )

    search_button = browser.find_element(
        By.XPATH, "//form[@class='search-form']/div[1]/i[@class='icon-search']"
    )

    browser.execute_script("arguments[0].click();", search_button)

    return browser
