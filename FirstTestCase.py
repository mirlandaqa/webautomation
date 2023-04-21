

#driver = webdriver.Chrome(executable_path="C:\chromedriver_updated\chromedriver.exe")

#Selenium 3
#driver.get("https://opensource-demo.orangehrmlive.com/")
#time.sleep(5)
#driver.find_element_by_name("username").send_keys("Admin")
#driver.find_element_by_name("password").send_keys("admin123")
#driver.find_element_by_class_name("orangehrm-login-action").click()

#act_title = driver.title
#exp_title = "OrangeHRMS"

#if (act_title==exp_title):
#   print("Login Test Passed")
#else:
# print("Login Test Failed")
#driver.close()
#

#Selenium 4
#from selenium.webdriver.chrome.service import Service
#servico_objeto=Service(executable_path="C:\chrome_webdriver\chromedriver.exe")

import time
from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_class_name("orangehrm-login-action").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()

