import time


from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://rahulsheetyacademy.com/angularpractice/")
driver.maximize_window()

dropdown = select(driver.find_element(By.ID,"exampleformcontrolselect1"))
dropdown.select_by_index(2)
time.sleep(5)
dropdown.slect_by_visible_text("female")



