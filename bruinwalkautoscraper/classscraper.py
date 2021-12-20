# other modules
from get_class_data import get_class_data
from enter_course import enter_course


# constants
from constants.dept_identifiers import dept_identifiers

# utils
from utils.utils import string_to_number

# libraries
from selenium import webdriver


dept_name = "Computer Science"
dept_keyword = dept_identifiers[dept_name]
classsearch_input_text = "CS 32"
class_number = string_to_number(classsearch_input_text)

browser = webdriver.Firefox()

browser.get("https://www.bruinwalk.com/search/")

# Returns a browser that has navigated to the correct course

browser = enter_course(
    browser, dept_name, dept_keyword, classsearch_input_text, class_number
)

# On the page of the desired course,
# scrape each of the pages belonging to the different professor

class_data = get_class_data(browser)

print(class_data)

browser.close()
