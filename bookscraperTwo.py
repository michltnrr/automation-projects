from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Safari()

time.sleep(1)
driver.maximize_window()
driver.get('https://registration.wayne.edu/StudentRegistrationSsb/ssb/registration')

# locates appropiate link
clsLnk = driver.find_element(By.ID, "classSearchLink")
webdriver.ActionChains(driver).double_click(clsLnk).perform()

#finds search box and selects class term

Btn = driver.find_element(By.CLASS_NAME, 'select2-chosen')
webdriver.ActionChains(driver).context_click(Btn).perform()

time.sleep(1)
term = driver.find_element(By.ID, '202209')
webdriver.ActionChains(driver).context_click(term).perform()

time.sleep(1)
Slctrm = driver.find_element(By.CLASS_NAME, "form-button")
webdriver.ActionChains(driver).double_click(Slctrm).perform()