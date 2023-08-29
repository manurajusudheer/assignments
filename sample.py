import send as send
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.google.co.in/")

driver.find_element(By.xpath,"//textarea[@id='APjFqb']")


driver.find_element(By.CSS_SELECTOR,"input[value='Google Search']")



