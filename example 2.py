from Tools.scripts import google
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.google.co.in/")

txtbox=driver.find_element(By.XPATH,"//a[@aria-label='Gmail']")
gmail = driver.find_element(By.LINK_TEXT,"gmail")
gmail.click()
driver.back()
