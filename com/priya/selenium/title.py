from selenium.webdriver import Chrome
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver_win32 (1)/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.youtube.com/")

driver.maximize_window()
#To print title
print(driver.title)

# TO print URL
print(driver.current_url)

# To print HTML
print(driver.page_source)