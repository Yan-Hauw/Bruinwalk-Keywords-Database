# libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def enter_course(
    browser, dept_input_text, dept_keyword, classsearch_input_text, class_number
):
    WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//form[@id='category_filter']/a[2]/label")
        )
    )

    classes_button = browser.find_element(
        By.XPATH, "//form[@id='category_filter']/a[2]/label"
    )

    classes_button.click()

    WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located((By.ID, "department"))
    )
    dept_dropdown = browser.find_element(By.ID, "department")
    dept_options_object = Select(dept_dropdown)
    dept_options_object.select_by_visible_text(dept_input_text)

    WebDriverWait(browser, 20).until(
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

    js = 'arguments[0].setAttribute("value", "' + classsearch_input_text + '")'
    browser.execute_script(js, search_box)

    WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//form[@class='search-form']/div[1]/i[@class='icon-search']")
        )
    )
    search_button = browser.find_element(
        By.XPATH, "//form[@class='search-form']/div[1]/i[@class='icon-search']"
    )

    browser.execute_script("arguments[0].click();", search_button)

    WebDriverWait(browser, 20).until(
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
