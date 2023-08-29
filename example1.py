from selenium import webdriver

driver=webdriver.Edge()
driver.get("https://www.google.co.in/")
print("current URL -" +driver.current_url)
print("tittle -" +driver.title)
print("browser name  -" +driver.name)



