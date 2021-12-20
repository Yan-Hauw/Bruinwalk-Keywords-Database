# libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def enter_course(browser, dept_keyword, class_number):

    # Wait for the web elements of desired class to appear
    # and click appropriate element

    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'title') and text()='"
                + dept_keyword
                + class_number
                + "']",
            )
        )
    )

    enter_course_button = browser.find_element(
        By.XPATH,
        "//div[contains(@class, 'title') and text()='"
        + dept_keyword
        + class_number
        + "']",
    )

    enter_course_button.click()

    return browser
