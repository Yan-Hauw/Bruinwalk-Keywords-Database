# libraries
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# constants
from constants.scraping_keywords import scraping_keywords


def scrape_page(url):

    browser = webdriver.Firefox()

    browser.get(url)

    text = ""

    dict = {}

    keywords = scraping_keywords

    for i in keywords:
        dict[i] = 0

    while True:

        if text:
            next_buttons = browser.find_elements(
                By.XPATH, "//div[@class='paginator']/span/a[2]"
            )

            if not len(next_buttons) or "disabled" in next_buttons[0].get_attribute(
                "class"
            ):
                break

            else:
                next_buttons[0].click()

        html_file = browser.page_source

        soup = BeautifulSoup(html_file, "html.parser")

        text = soup.get_text()

        text = re.sub(r"[^a-zA-Z ]", "", text)

        words = text.split()

        for w in words:
            for i in keywords:
                if i in w:
                    dict[i] = dict[i] + 1 if i in dict else 1

    browser.close()

    return dict
