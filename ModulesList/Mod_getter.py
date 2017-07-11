from selenium import webdriver
import os

path = os.getcwd()
path = path + "/chromedriver"

driver = webdriver.Chrome(path)
driver.get("https://docs.python.org/3/py-modindex.html")

a = driver.find_elements_by_class_name('xref')
for i in a:
    print(i.text)
driver.quit()
