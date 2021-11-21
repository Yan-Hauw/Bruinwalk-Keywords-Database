# other modules
from bruinwalkautoscraper.get_class_data import get_class_data
from enter_course import enter_course


# constants
from constants.dept_keywords import dept_identifiers

# utils
from utils.utils import string_to_number

# libraries
from selenium import webdriver


dept_input_text = "Linguistics"
dept_keyword = dept_identifiers[dept_input_text]
classsearch_input_text = "Ling 1"
class_number = string_to_number(classsearch_input_text)

browser = webdriver.Firefox()

browser.get("https://www.bruinwalk.com/search/")

browser = enter_course(
    browser, dept_input_text, dept_keyword, classsearch_input_text, class_number
)

class_data = get_class_data(browser, dept_keyword, class_number)


browser.close()
