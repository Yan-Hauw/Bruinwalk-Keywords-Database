# other modules
from pagescraper import scrape_page

# libraries
from selenium.webdriver.common.by import By


def get_class_data(browser):
    class_data = []

    while True:

        course_professor_anchors = browser.find_elements(By.XPATH, "//tr/*[2]/a")

        urls = []

        for a in course_professor_anchors:
            urls.append(a.get_attribute("href"))

        professor_spans = browser.find_elements(
            By.XPATH, "//a/*[1][@class='prof name']"
        )

        for span in professor_spans:
            url = urls.pop(0)
            results = scrape_page(url)
            res_tuple = (span.text, results)
            class_data.append(res_tuple)

        next_button = browser.find_element(
            By.XPATH, "//div[@class='paginator']/span/a[2]"
        )
        if "disabled" in next_button.get_attribute("class"):
            break
        else:
            next_button.click()

    return class_data
