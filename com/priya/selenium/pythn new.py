from selenium.webdriver import Chrome
import logging
path="C:/Users/User/PycharmProjects/pythonSelenium/drivers1/chromedriver_win32 (1)/chromedriver.exe"
driver=Chrome(executable_path=path)

#step 2

log=logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#step3
warn=logging.FileHandler('warning_logs.txt')
warn.setLevel(logging.WARNING)

info=logging.FileHandler('INFOR_logs.txt')
info.setLevel(logging.INFO)

#STEP4
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# step5
warn.setFormatter(formatter)
info.setFormatter(formatter)

driver.maximize_window()
driver.get("https://www.theTestingworld.com/testings")
log.info("[my url is opened]")
log.warning("[delay in opening web]")
