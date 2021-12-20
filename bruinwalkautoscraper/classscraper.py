# other modules
from get_class_data import get_class_data

# libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def scrape_class(browser, course_name):

    # Wait for the web elements of desired class to appear
    # and click appropriate element

    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'title') and text()='" + course_name + "']",
            )
        )
    )

    enter_course_button = browser.find_element(
        By.XPATH,
        "//div[contains(@class, 'title') and text()='" + course_name + "']",
    )

    enter_course_button.click()

    # On the page of the desired course,
    # scrape each of the pages belonging to the different professor
    class_data = get_class_data(browser)

    browser.close()

    return class_data
