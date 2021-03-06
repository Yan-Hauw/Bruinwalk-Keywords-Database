# other modules
from load_table import load_table
from create_table import create_table
from convert_to_loadfile import convert_to_loadfile
from classscraper import scrape_class
from courselist_locate import locate_course
from generate_courses import generate_dept_course_list


# constants
from constants.courses_by_dept import courses_by_dept


# libraries
from selenium import webdriver


dept_name = "Computer Science"
list_of_courses = courses_by_dept[dept_name]

browser = webdriver.Firefox()

browser.get("https://www.bruinwalk.com/search/")

# Search by department name, list all courses from that dept

browser = generate_dept_course_list(browser, dept_name)

all_results = []

# for all courses we want to scrape
for course in list_of_courses:
    # locate course
    browser = locate_course(browser, course)

    url = browser.current_url

    new_browser = webdriver.Firefox()

    new_browser.get(url)

    course_keywords = scrape_class(new_browser, course)

    all_results.append(course_keywords)

convert_to_loadfile(all_results)

dept_name = dept_name.lower()

dept_name = dept_name.replace(" ", "_")

print(dept_name)

create_table(dept_name)

load_table(dept_name)


print(all_results)

browser.close()
