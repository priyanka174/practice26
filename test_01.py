from selenium.webdriver import Chrome
def test_data():
    path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.naukri.com/")
    driver.close()

def test_FB():
    path = "C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    driver.close()


#conditionally skip execution

from selenium.webdriver import Chrome
import pytest
a=100


def test_data():
    path = "C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.naukri.com/")
    driver.close()

@pytest.mark.skipif(a>=100,reason="dont execcute")
def test_FB():
    path = "C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    driver.close()


Goruping testcases:
from selenium.webdriver import Chrome
import pytest

@pytest.mark.Smoke
def test_data():
    path = "C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.naukri.com/")
    driver.close()

@pytest.mark.Sanity
def test_FB():
    path = "C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    driver.close()



Fixtures:
from selenium.webdriver import Chrome
@pytest.fixture()
def setpath():
    global driver
    path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.thetestingworld.com/testings")
    yield
    driver.close()

def test_fi(setpath):
    driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("srishanth")
    driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("srishanth@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("12345678")

def test_fx(setpath):
    driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("srishanth")
    driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("srishanth@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("12345678")
    driver.find_element_by_xpath("//input[@name='fld_cpassword']").send_keys("12345678")
    driver.find_element_by_xpath("//input[@name='dob']").send_keys("12/12/1998")
    driver.find_element_by_xpath("//input[@name='phone']").send_keys("7624963454")
    driver.find_element_by_xpath("//input[@name='dob']").send_keys("kolar")

