'''from selenium.webdriver import Chrome
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
driver=Chrome(executable_path=path)

#driver.get("https://www,thetestingworld.com/testings")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_xpath("//a[contains(text(), 'Create a Page')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Sign Up')]").click()
driver.find_element_by_name("firstname").send_keys("priya")'''


from selenium.webdriver import Chrome
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
        driver.find_element_by_xpath("//button[text()='Start Download']").click()