'''from selenium.webdriver import Chrome

#To import Action Chains
from selenium.webdriver.common.action_chains import ActionChains

# To import special chains
from selenium.webdriver.common.keys import Keys
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver_win32 (1)/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.find_element_by_name("firstname").send_keys("priya")
act=ActionChains(driver)
act.send_keys(Keys.BACK_SPACE).perform()'''



from selenium.webdriver import Chrome

#To import Action Chains
from selenium.webdriver.common.action_chains import ActionChains

# To import special chains
from selenium.webdriver.common.keys import Keys
import time
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver_win32 (1)/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.find_element_by_name("firstname").send_keys("priya")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").perform()
time.sleep(4)
act.key_down(Keys.CONTROL).send_keys("x").perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys("v").perform()
