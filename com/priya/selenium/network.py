'''from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
driver=Chrome(executable_path=path)
path=""
driver.get("https://www,thetestingworld.com/testings")
driver.maximize_window()
obj=Select(driver.find_element_by_name('sex'))
obj.select_by_visible_text('male')
act=ActionChains(driver)
act.send_keys(a)
act.click()
driver.implicitly_wait(20)
driver.set_page_load_timeout(12)
wait=WebDriverWait(driver.100)
wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'), India))'''


from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
path=""
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
obj=Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("male")

act=ActionChains(driver)
act.send_keys('a').perform()
act.key_down(Keys.CONTROL).key_down('a').send_keys(Keys.DELETE).perform()

driver.set_page_load_timeout()
wait=WebDriverWait(driver,100)
wait.until(ec.text_to_be_present_in_element((By.ID, 'CountryId'),"india"))


alwindow=driver.window_handles
for win in alwindow:
    driver.switch_to_window(win)
    print(driver.current_url)
    if(driver.current_url==https:www.naukri.com/):
        mainwin=win
    else:
        driver.close
    driver.switch_to_window(mainwin





