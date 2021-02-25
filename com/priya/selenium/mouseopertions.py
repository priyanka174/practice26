from selenium.webdriver import Chrome

#To import Action Chains
from selenium.webdriver.common.action_chains import ActionChains

# To import special chains
from selenium.webdriver.common.keys import Keys
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver_win32 (1)/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
#to maximize browser
driver.maximize_window()
act = ActionChains(driver)
#To perform left click operation
act.click().perform() #left click
#TO prform left click operation on specific position
act.context_click(driver.find_element_by_name("firstname")).perform()
#To perform right click operation
act.context_click().perform()
#To perform right cick operation on spescific position
act.context_click(driver.find_element_by_name("firstname")).perform()

#To perform double clock operation
act.double_click().perform()
#To perform double click on specific position
act.double_click(driver.find_element_by_name("firstname")).perform()

#Moving mouse to the menu so menu will open
act.move_to_element(driver.find_element_by_name("birthday_day")).perform()





#mouse move action
from selenium.webdriver import Chrome

#To import Action Chains
from selenium.webdriver.common.action_chains import ActionChains

# To import special chains
from selenium.webdriver.common.keys import Keys
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver_win32 (1)/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.theTestingworld.com/")
#to maximize browser
driver.maximize_window()
act = ActionChains(driver)
#To perform left click operation
#act.click().perform() #left click
#TO prform left click operation on specific position
act.move_to_element(driver.find_element_by_xpath("//span[contains(text(), 'TUTORIAL')]")).perform()