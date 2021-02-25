from selenium import webdriver
import time
driver = webdriver.Chrome("C:/Users/User/PycharmProjects/pythonSelenium/drivers/chromedriver_win32 (1)/chromedriver.exe")
driver.set_page_load_timeout("10")
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("python step by step tutorials")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit()


C:\Users\User\Downloads\chromedriver_win32 (1)
C:\Users\User\Downloads\chromedriver_win32 (1)

