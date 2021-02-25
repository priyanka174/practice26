'''from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By

path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()
obj=Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")
wait=WebDriverWait(driver,100)
wait.until(ec.text_to_be_present_in_element((By.ID, 'countryId'),'India'))
obj=Select(driver.find_element_by_id("countryId"))
obj.select_by_visible_text("India")
wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), 'Karnataka'))
obj=Select(driver.find_element_by_id("stateId"))
obj.select_by_visible_text("Karnataka")'''


'''from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com")
driver.maximize_window()
act=ActionChains(driver)
#act.click().perform()
#act.context_click().perform()
#act.double_click().perform()
#act.click_and_hold().perform()
act.click(driver.find_element_by_xpath("//a[contains(text(),'Registration')]")).perform()
ac'''

from selenium.webdriver import Chrome
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.naukri.com")
driver.maximize_window()
main=""
alwindows=driver.window_handles
print(alwindows)
for i in alwindows:
    driver.switch_to_window(i)

    if(driver.current_url=="https://www.naukri.com/"):
        driver.find_element_by_id("qsb-keyword-sugg").send_keys("IT jobs")
        driver.find_element_by_id("qsb-location-sugg").send_keys("Bangalore")
        driver.find_element_by_class_name("btn").click()
        driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/pythonSelenium/screen/ss.png")
    else:
        driver.close()





