# libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def generate_dept_course_list(browser, dept_name):

    # Click the classes button

    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//form[@id='category_filter']/a[2]/label")
        )
    )

    classes_button = browser.find_element(
        By.XPATH, "//form[@id='category_filter']/a[2]/label"
    )

    classes_button.click()

    # Wait for department dropdown and select appropriate option

    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located((By.ID, "department"))
    )

    dept_dropdown = browser.find_element(By.ID, "department")
    dept_options_object = Select(dept_dropdown)
    dept_options_object.select_by_visible_text(dept_name)

    return browser
