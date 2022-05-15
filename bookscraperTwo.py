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

# inputs major 
mjrBox = driver.find_element(By.CLASS_NAME, 'select2-choices')
webdriver.ActionChains(driver).double_click(mjrBox).perform()
mjrBox = driver.find_element(By.CLASS_NAME, 'select2-choices').send_keys('psychology')
time.sleep(1)

#selects item from dropdown
mjrBox = driver.find_element(By.CLASS_NAME, 'select2-choices').send_keys(Keys.DOWN)
mjrBox = driver.find_element(By.CLASS_NAME, 'select2-choices').send_keys(Keys.ENTER)
sch = driver.find_element(By.ID, 'search-go')
webdriver.ActionChains(driver).double_click(sch).perform()

#finds class
crs = driver.find_element(By.LINK_TEXT, "Introductory Psychology")
crs = driver.find_element(By.LINK_TEXT, "Introductory Psychology").send_keys(Keys.ENTER)

#copies course data
# sectionNum1 = driver.find_element(By.ID, 'sectionNumber')
# webdriver.ActionChains(driver).double_click(sectionNum1).key_down(Keys.META).send_keys('c').perform()


xOffset = 734
yOffset = 292
webdriver.ActionChains(driver).move_by_offset(xOffset,yOffset).key_down(Keys.META).send_keys('c').perform()
