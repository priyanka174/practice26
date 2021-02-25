'''from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()
driver.find_element_by_name("fld_username").send_keys("priynks")
act=ActionChains(driver)
act.send_keys(Keys.ENTER).perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys("a")
act.key_down(Keys.CONTROL).send_keys("x")'''



'''from selenium.webdriver import Chrome
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("srishanth")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("srishanth@gmail.com")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("12345678")
driver.find_element_by_xpath("//input[@name='fld_cpassword']").send_keys("12345678")
driver.find_element_by_xpath("//input[@name='dob']").send_keys("12/12/1998")
driver.find_element_by_xpath("//input[@name='phone']").send_keys("7624963454")
driver.find_element_by_xpath("//input[@name='dob']").send_keys("kolar")
driver.find_element_by_xpath("//input[@name='add_type']").click()
#obj=Select(driver.find_elements_by_name("sex"))
obj=Select (driver.find_element_by_name("sex"))
obj.select_by_index(1)

obj=Select(driver.find_element_by_name("country"))
obj.select_by_visible_text("India")
#obj=Select(driver.find_elements_by_name("country"))
#obj.select_by_value(3)
#obj.select_by_visible_text("India")
obj=Select(driver.find_elements_by_name("city"))
obj.select_by_visible_text(karanatake)
obj=Select(driver.find_elements_by_name("state"))
time.sleep(5)
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()
driver.find_element_by_name("fld_username").send_keys("priya")
#driver.find_element_by_name("fld_username").send_keys("priynks")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).key_down('a').send_keys(Keys.DELETE).perform()
time.sleep(5)
driver.close()'''



'''from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com")
driver.maximize_window()
act=ActionChains(driver)
#act.context_click(driver.find_elements_by_id("menu435")).perform()

#act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()
time.sleep(5)
driver.close()'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()'''
'''print(driver.title)
print(driver.current_url)
print(driver.page_source)'''
'''print("the text on link is:-" +driver.find_element_by_class_name("displayPopup").text)
print(driver.find_element_by_xpath("//input[@name='fld_username']").get_attribute("field"))'''

'''from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("priya")
driver.find_element_by_name("fld_username").send_keys("priya")
driver.find_element_by_xpath("//input[@placeholder='myusername@gmail.com']").send_keys("npriyanka3006@gmail.com")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("12345678")
driver.find_element_by_xpath("//input[@name='fld_cpassword']").send_keys("12345678")
driver.find_element_by_xpath("//input[@name='dob']").send_keys("12/12/1998")
driver.find_element_by_xpath("//input[@name='phone']").send_keys("7624963454")
driver.find_element_by_xpath("//input[@name='dob']").send_keys("kolar")
driver.find_element_by_xpath("//input[@value='office']").click()
obj=Select(driver.find_element_by_xpath("//select[@name='sex']"))
obj.select_by_value("2")
obj=Select(driver.find_element_by_name("country"))
obj.select_by_visible_text("India")
driver.find_element_by_name("zip").send_keys("563135")
driver.find_element_by_name("terms").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.close()'''


'''from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/")
driver.maximize_window()
act=ActionChains(driver)
#act.context_click(driver.find_element_by_xpath("//span[@class='menu-title'])").perform()
act.move_to_element(driver.find_element_by_xpath("//span[text()='VIDEOS ']")).perform()
time.sleep(3)
driver.close()

from selenium.webdriver import Chrome
def test_reg_01():
    path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    driver.close()'''








