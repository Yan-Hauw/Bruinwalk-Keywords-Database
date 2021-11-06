import sys
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


browser = webdriver.Firefox()


browser.get("https://www.bruinwalk.com/professors/parvaneh-ghaforyfrd/com-sci-33/")

text = ""

dict = {}

while True:

    if text:
        next_button = browser.find_element(
            By.XPATH, "//div[@class='paginator']/span/a[2]"
        )
        if "disabled" in next_button.get_attribute("class"):
            print("break")
            break
        else:
            print("click")
            next_button.click()

    html_file = browser.page_source

    soup = BeautifulSoup(html_file, "html.parser")

    keywords = {"slides", "textbook"}

    text = soup.get_text()

    text = re.sub(r"[^a-zA-Z ]", "", text)

    words = text.split()

    for w in words:
        for i in keywords:
            if i in w:
                dict[i] = dict[i] + 1 if i in dict else 1

    print("success")


print(dict)

browser.close()
