from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:/Users/User/PycharmProjects/pythonSelenium/drivers/geckodriver.exe")

driver.set_page_load_timeout("10")
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("python step by step tutorials")
driver.find_element_by_name("btnk").click()
time.sleep(4)
driver.quit()