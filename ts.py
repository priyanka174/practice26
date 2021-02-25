'''def takess(driver, name):
    driver.get_screnshot_as_file("def take_page_ss(driver, name):
    driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/pythonSelenium/ss1.png" +name+".png")")'''



from selenium.webdriver import Chrome
#To work on dropdown
from selenium.webdriver.support.select import Select
#To work on keyboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#To work on explicit wait:

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By

path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://wwww.thetestingworld.com/testings")
driver.maximize_window()
obj=Select(driver.find_elements_by_name("sex"))
obj.select_by_visible_text('male')
driver.find_element_by_xpath("fid_username").send_keys("priya")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a')

#mouse operations:

act=ActionChains(driver)
act.click(driver.find_element_by_xpath("//span[@text()='Login']"))
act.context_click()
act.move_to_element()


pageload:
driver.set_page_load_timeout(1)
Explicit wait:
wait=WebDriverWait(driver,100)
wait.until(ec.text_to_be_present_in_element((By.ID, 'countryId'), 'India'))
obj=Select(driver.find_element_by_id('countryId'))
obj.select_by_visible_text('India')
wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'),'Karnataka'))
obj=Select(driver.find_element_by_id('StateId'))
obj.select_by_visible_text('Karnataka')


#to take SS

driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/pythonSelenium/ss.png")