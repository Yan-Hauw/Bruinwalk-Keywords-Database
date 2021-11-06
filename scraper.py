import sys
import re

from selenium import webdriver
from bs4 import BeautifulSoup


browser = webdriver.Firefox()


browser.get("https://www.bruinwalk.com/professors/junghoo-cho/com-sci-143/")

html_file = browser.page_source

soup = BeautifulSoup(html_file, "html.parser")

keywords = {"slides", "textbook"}

dict = {}


text = soup.get_text()

text = re.sub(r"[^a-zA-Z ]", "", text)

words = text.split()

for w in words:
    for i in keywords:
        if i in w:
            dict[i] = dict[i] + 1 if i in dict else 1


print(dict)

browser.close()
