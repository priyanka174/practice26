# to youtube

from selenium.webdriver import Chrome
path="C:/Users/User/Downloads/chromedriver_win32 (2)/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.youtube.com/")
driver.find_element_by_name("search_query").send_keys("selenium with python")
driver.find_element_by_id("search-icon-legacy").click()

# for facebook sign up

'''from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver_win32 (1)/chromedriver.exe"
driver= Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.find_element_by_name("firstname").send_keys("priya")
driver.find_element_by_name("lastname").send_keys("nN")
driver.find_element_by_name("reg_email__").send_keys("npriyanka3006@gmail.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("npriyanka3006@gmail.com")
driver.find_element_by_name("reg_passwd__").send_keys("1234567")
#working on dropdown
obj=Select(driver.find_element_by_id("day"))
obj.select_by_visible_text("30")
obj=Select(driver.find_element_by_id("month"))
obj.select_by_visible_text("Jun")
obj=Select(driver.find_element_by_id("year"))
obj.select_by_visible_text("1997")

#working on radio button using xpath
driver.find_element_by_xpath("//input[@value='2']").click()
#working on radio button
#driver.find_element_by_name("sex").click()
#working on button
driver.find_element_by_id("u_0_13").click()
# wprking on link
#driver.find_element_by_id("privacy-link").click()'''

#To work on firefox

from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/geckodriver-v0.26.0-win64 (1)/geckodriver.exe"
driver= Firefox(executable_path=path)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_name("firstname").send_keys("priya")
driver.find_element_by_name("lastname").send_keys("nN")
driver.find_element_by_name("reg_email__").send_keys("npriyanka3006@gmail.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("npriyanka3006@gmail.com")
driver.find_element_by_name("reg_passwd__").send_keys("1234567")
#working on dropdown
obj=Select(driver.find_element_by_id("day"))
obj.select_by_visible_text("30")
obj=Select(driver.find_element_by_id("month"))
obj.select_by_visible_text("Jun")
obj=Select(driver.find_element_by_id("year"))
obj.select_by_visible_text("1997")

#working on radio button using xpath
driver.find_element_by_xpath("//input[@value='2']").click()
#working on radio button
#driver.find_element_by_name("sex").click()
#working on button
driver.find_element_by_id("u_0_13").click()
# wprking on link
#driver.find_element_by_id("privacy-link").click()

