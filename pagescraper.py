import re


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup


browser = webdriver.Firefox()


browser.get("https://www.bruinwalk.com/professors/junghoo-cho/com-sci-143/")

text = ""


dict = {}

WebDriverWait(browser, 20).until(
    expected_conditions.presence_of_element_located(
        (By.XPATH, "//div[@class='paginator']/span/a[2]")
    )
)

while True:

    if text:
        next_button = browser.find_element(
            By.XPATH, "//div[@class='paginator']/span/a[2]"
        )
        if "disabled" in next_button.get_attribute("class"):

            break
        else:

            next_button.click()

    html_file = browser.page_source

    soup = BeautifulSoup(html_file, "html.parser")

    keywords = {"slide", "upload", "post", "attendance", "pair", "partner", "together"}

    text = soup.get_text()

    text = re.sub(r"[^a-zA-Z ]", "", text)

    words = text.split()

    for w in words:
        for i in keywords:
            if i in w:
                dict[i] = dict[i] + 1 if i in dict else 1

print(dict)

browser.close()
