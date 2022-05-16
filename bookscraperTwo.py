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

# time.sleep(1)
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

#finds class data

numLnk = driver.find_element(By.LINK_TEXT, 'Linked Sections')
webdriver.ActionChains(driver).click(numLnk).perform()
time.sleep(5)

# copies & saves class data 
findNum = driver.find_element(By.XPATH, "//table[@class='basePreqTable']") #enter tag, and unique element 
webdriver.ActionChains(driver).move_to_element(findNum).click(findNum).key_down(Keys.META).send_keys('c').perform()

time.sleep(1)
driver.switch_to.new_window('tab')
driver.get('https://wayne.bncollege.com/?utm_source=google&utm_medium=cpc&utm_campaign=Act740%3EPar740%3EWayne+State+University%3ESX%3EBook+Store&s_kwcid=AL!14348!3!565956682773!e!!g!!wayne%20state%20bookstore&gclsrc=aw.ds&gclid=EAIaIQobChMIgeiSyJLi9wIVuRPUAR1-dAwpEAAYASAAEgJTQfD_BwE')
driver.fullscreen_window()

#enters copied data into bookstore
time.sleep(1)
bkLnk = driver.find_element(By.XPATH, "//a[@title='Course Materials & Textbooks']")
webdriver.ActionChains(driver).click(bkLnk).perform()

books = driver.find_element(By.XPATH, "//a[@title='Find Course Materials']")
webdriver.ActionChains(driver).click(books).perform()

#copying 
time.sleep(5)
term = driver.find_element(By.XPATH, "//span[@role='combobox']")
webdriver.ActionChains(driver).move_to_element(term).click(term).perform()
term = driver.find_element(By.XPATH, "//span[@role='combobox']").send_keys(Keys.DOWN)
term = driver.find_element(By.XPATH, "//span[@role='combobox']").send_keys(Keys.ENTER)

time.sleep(1) 
# center = driver.find_element(By.XPATH, "//span[@title='Official Online Store of Wayne State University']")
sbJct = driver.find_element(locate_with(By.TAG_NAME, "span").to_right_of(term))
webdriver.ActionChains(driver).click(sbJct).perform()

# sbJct = driver.find_element(By.XPATH, "//b[@role='presentation']").send_keys('PSY')
# sbJct = driver.find_element(By.XPATH, "//b[@role='presentation']").send_keys(Keys.ENTER)



# term = driver.find_element(By.XPATH, "//span[@title= ' Select']").send_keys(Keys.DOWN)
# term = driver.find_element(By.XPATH, "//span[@title= ' Select']").send_keys(Keys.ENTER)
