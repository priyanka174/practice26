'''from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
wait.until(ec.text_to_be_present_in_element((By.NAME, "country"), 'India'))
obj=Select(driver.find_element_by_name("country"))
obj.select_by_visible_text("India")

driver.find_element_by_name("zip").send_keys("563135")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()

driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/pythonSelenium/practise.png")'''
from selenium.webdriver import Chrome
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.naukri.com/")
driver.maximize_window()
mainvariable=""
Alwindows=driver.window_handles
print(Alwindows)
for win in Alwindows:
    driver.switch_to_window(win)
    if(driver.current_url=="https://www.naukri.com/"):
        mainvariable=win
    else:
        driver.close()
driver.switch_to_window(mainvariable)
driver.find_element_by_id("qsb-keyword-sugg").send_keys("ITjobs")
driver.find_element_by_id("qsb-location-sugg").send_keys("Bagalore")
driver.find_element_by_xpath("//button[text()='Search']").click()






