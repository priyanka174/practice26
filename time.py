'''from selenium.webdriver import Chrome
import ss
path="C:/Users/User/PycharmProcts/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()'''

'''from selenium.webdriver import Chrome
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.naukri.com")
driver.maximize_window()
mainwin=""
Alwindow=driver.window_handles
for win in Alwindow:
    driver.switch_to.window(win)
    if(driver.current_url=="https://www.naukri.com/"):
        mainwin=win
    else:
        driver.close()
driver.switch_to.window(mainwin)
print(driver.current_url)'''

'''from selenium.webdriver import Chrome
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings")
driver.maximize_window()
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[type='submit' or @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
driver.find_element_by_xpath("//a[text()='Delete']").click()
alltabs=driver.window_handles
for win in alltabs:
    driver.switch_to_window(win)
    print(driver.current_url)
    if(driver.current_url=="https://www.thetestingworld.com/testings/manage_customer.php"):
        driver.find_element_by_xpath("//button[text()='Start Download']").click()'''



'''from selenium.webdriver import Chrome
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.naukri")

driver.maximize_window()
mainwin=""
alwindow=driver.window_handles
for win in alwindow:
    driver.switch_to_window(win)
    if(driver.current_url=="https://www.naukri.com/"):

        mainwin(win)
    else:
        driver.close()
driver.switch_to_window(mainwin)
print(driver.current_url)'''

from selenium.webdriver import Chrome
import ss
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.naukri.com/")

driver.maximize_window()
ss.takess(driver, "naukariss")
