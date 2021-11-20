# other modules
from enter_course import enter_course

from pagescraper import scrape_page

# constants
from constants.dept_keywords import dept_identifiers

# utils
from utils.utils import string_to_number

# libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


dept_input_text = "Linguistics"
dept_keyword = dept_identifiers[dept_input_text]
classsearch_input_text = "Ling 1"
class_number = string_to_number(classsearch_input_text)

browser = webdriver.Firefox()

browser.get("https://www.bruinwalk.com/search/")

browser = enter_course(
    browser, dept_input_text, dept_keyword, classsearch_input_text, class_number
)

class_data = []

while True:

    course_professor_anchors = browser.find_elements(By.XPATH, "//tr/*[2]/a")

    urls = []

    for a in course_professor_anchors:
        urls.append(a.get_attribute("href"))

    professor_spans = browser.find_elements(By.XPATH, "//a/*[1][@class='prof name']")

    for span in professor_spans:
        url = urls.pop(0)
        results = scrape_page(url)
        res_tuple = (dept_keyword + class_number, span.text, results)
        class_data.append(res_tuple)

    next_button = browser.find_element(By.XPATH, "//div[@class='paginator']/span/a[2]")
    if "disabled" in next_button.get_attribute("class"):
        break
    else:
        next_button.click()

print(len(class_data))

print(class_data)


browser.close()
