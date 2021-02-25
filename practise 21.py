from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path==path)
driver.get("https://www.thetestingworld.com/testings")
obj=Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("priya")
driver.find_element_by_name("fld_username").send_keys("priya")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).key_down('a').send_keys(Keys.DELETE).perform()


from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.testingworld.com")
act=ActionChains(driver)
act.click().perform()
act.context_click().perform()
act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
act.context_click(driver.find_element_by_xpath("//a[text()='Login']"))
act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()




#waits

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.set_page_load_timeout(20)
driver.get("https://www.testingworldcom/testings")
driver.set_page_load_timeout(20)
wait=WebDriverWait(driver,100)
wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),'India'))
obj=Select(driver.find_element_by_name("countryId"))
obj.select_by_visible_text("India")
wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),'Karnataka'))
obj=Select(driver.find_element_by_name("stateId"))
obj.select_by_visible_text("Karnataka")


#multiwindow hadloing:

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)

driver.get("https://www.naukri.com")
Alwindows=driver.window_handles
print(Alwindows)
for win in Alwindows:
    driver.switch_to_window(win)
    print(driver.current_url)

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)

driver.get("https://www.naukri.com")
Alwindows=driver.window_handles
for win in Alwindows
    driver.switch_to_window(win)
    if(driver.current_url=="https://www.naukri.com/")
        print("this is main window")
    else:
        driver.close()

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.maximize_window()
mainvar=""
driver.get("https://www.naukri.com/")
Alwindows=driver.window_handles
for win in Alwindows:
    driver.switch_to_window(win)
    if(driver.current_url=="https:www.naukri.com/"):
        mainvar=win
    else:
        driver.close()
driver.switch_to_window(mainvar)
print(driver.current_url)


screenshot:

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.maximize_window()

driver.get("https://www.naukri.com/")
driver.get_screenshot_as_file("C:\Users\User\PycharmProjects\pythonSelenium/practise21.png")















