from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
import time
driver = webdriver.Safari()
time.sleep(1)
driver.fullscreen_window()
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


# copies course and section number 
time.sleep(1)
crsNum = driver.find_element(By.XPATH, "//span[@id='courseNumber']").text 
time.sleep(1)
sctnNum = driver.find_element(By.XPATH, "//span[@id='sectionNumber']").text
orignial_window = driver.current_window_handle #stores current window to switch back later
time.sleep(1)
driver.switch_to.new_window('tab')
driver.get('https://wayne.bncollege.com/?utm_source=google&utm_medium=cpc&utm_campaign=Act740%3EPar740%3EWayne+State+University%3ESX%3EBook+Store&s_kwcid=AL!14348!3!565956682773!e!!g!!wayne%20state%20bookstore&gclsrc=aw.ds&gclid=EAIaIQobChMIgeiSyJLi9wIVuRPUAR1-dAwpEAAYASAAEgJTQfD_BwE')
driver.fullscreen_window()

#enters copied data into bookstore
time.sleep(1)
second_window = driver.current_window_handle #store 
bkLnk = driver.find_element(By.XPATH, "//a[@title='Course Materials & Textbooks']")
webdriver.ActionChains(driver).click(bkLnk).perform()

books = driver.find_element(By.XPATH, "//a[@title='Find Course Materials']")
webdriver.ActionChains(driver).click(books).perform()

#copying (chooses term)
time.sleep(3)
term = driver.find_element(By.XPATH, "//span[@role='combobox']")
webdriver.ActionChains(driver).move_to_element(term).click(term).perform()
term = driver.find_element(By.XPATH, "//span[@role='combobox']").send_keys(Keys.DOWN)
term = driver.find_element(By.XPATH, "//span[@role='combobox']").send_keys(Keys.ENTER)

# chooses class dept.
time.sleep(1) 
sbJct = driver.find_element(locate_with(By.TAG_NAME, "span").to_right_of({By.XPATH: "//span[@role='combobox']"}))
time.sleep(1)
webdriver.ActionChains(driver).send_keys(Keys.TAB).perform() #idk if assing a value to this action is sustainable
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
drpMnt = driver.find_element(By.XPATH, "//input[@type='search']").send_keys('PSY')
drpMnt = driver.find_element(By.XPATH, "//input[@type='search']").send_keys(Keys.ENTER)

#pastes in copied courseNum
time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.TAB *2).perform()
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# SpcNum = driver.find_element(By.XPATH, "//input[@type='search']")
# SpcNum = driver.find_element(By.XPATH, "//input[@type='search']").key_down(Keys.META).send_keys('v').perform()
# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
webdriver.ActionChains(driver).key_down(Keys.META).send_keys(crsNum).perform() #coursenumer is pasted
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
webdriver.ActionChains(driver).key_down(Keys.META).send_keys(sctnNum).perform() #sectionnumber is pasted
# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()



#back to tab copy and paste class section


# time.sleep(1)
# driver.switch_to.window(orignial_window)
# webdriver.ActionChains(driver).double_click().perform()
# time.sleep(1)
# # webdriver.ActionChains(driver).double_click().perform()
# # sctnNum = driver.find_element(By.XPATH, "//span[@id='sectionNumber']").text
# time.sleep(1)
# driver.switch_to.window(second_window)
# time.sleep(2)
# webdriver.ActionChains(driver).double_click().perform()
# time.sleep(2)



# webdriver.ActionChains(driver).click(term).perform()
# webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
# time.sleep(3)
# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# webdriver.ActionChains(driver).send_keys(Keys.TAB *3).perform()
# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# webdriver.ActionChains(driver).key_down(Keys.META).send_keys(sctnNum).perform()

