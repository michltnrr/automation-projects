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

# crs = driver.find_element(By.LINK_TEXT, "Introductory Psychology")
# crs = driver.find_element(By.LINK_TEXT, "Introductory Psychology").send_keys(Keys.ENTER)
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()


# copies coursenumber and course reference number 
time.sleep(1)


# Refnum = driver.find_element(By.XPATH, "//span[@id='courseReferenceNumber']").text
# webdriver.ActionChains(driver).move_to_element(Refnum).double_click(Refnum).key_down(Keys.META).send_keys('c').perform()
time.sleep(1)

crsNum = driver.find_element(By.XPATH, "//span[@id='courseNumber']").text 
time.sleep(1)
# Lnk = driver.find_element(By.LINK_TEXT, 'Linked Sections')
# webdriver.ActionChains(driver).click(Lnk).perform()
time.sleep(1)

# sctnNum = driver.find_element(By.XPATH, "//span[@id='sectionNumber']").text
# orignial_window = driver.current_window_handle #stores current window to switch back later
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

# time.sleep(1) 
# sbJct = driver.find_element(locate_with(By.TAG_NAME, "span").to_right_of({By.XPATH: "//span[@role='combobox']"}))
time.sleep(1)
webdriver.ActionChains(driver).send_keys(Keys.TAB).perform() #idk if assing a value to this action is sustainable
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
webdriver.ActionChains(driver).send_keys('PSY').perform()
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# drpMnt = driver.find_element(By.XPATH, "//input[@type='search']").send_keys('PSY')
# drpMnt = driver.find_element(By.XPATH, "//input[@type='search']").send_keys(Keys.ENTER)


#pastes in copied courseNum

time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.TAB *2).perform()
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# SctnmBox = driver.find_element(By.XPATH, "//input[@type='search']")
# SpcNum = driver.find_element(By.XPATH, "//input[@type='search']")
# SpcNum = driver.find_element(By.XPATH, "//input[@type='search']").key_down(Keys.META).send_keys('v').perform()
# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
webdriver.ActionChains(driver).key_down(Keys.META).send_keys(crsNum).perform() #coursenumber is pasted
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()


time.sleep(2)

# webdriver.ActionChains(driver).send_keys(Keys.TAB *2).perform()
# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(4)
# webdriver.ActionChains(driver).send_keys(Keys.TAB *10).perform()
# webdriver.ActionChains(driver).key_down(Keys.META).send_keys(sctnNum).perform() #sectionnumber is pasted
clearBtn = driver.find_element(By.XPATH, "//a[@class='js-clear-row']")
SctnmBox = driver.find_element(locate_with(By.XPATH, "//span[@role='textbox']").to_left_of({By.XPATH: "//a[@class='js-clear-row']"})) #.send_keys(sctnNum).perform()
webdriver.ActionChains(driver).click(SctnmBox).perform()
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(2)



#scroll to bottom of page and click 'retrive materials' link 


driver.execute_script("document.getElementById('email_id_desktop').scrollIntoView();")

time.sleep(3)

getLnk = driver.find_element(locate_with(By.XPATH, "//a[@role='link']").to_right_of({By.XPATH: "//div[@class='bned-btn-text']"}))
webdriver.ActionChains(driver).click(getLnk).perform()


# add book to cart

# time.sleep(4)

# # driver.execute_script()
time.sleep(3)
wrkRnd = driver.find_element(locate_with(By.XPATH, "//a[@role='button']").below({By.XPATH: "//span[@class='bned-capitalize']"}))
# wrkRnd = driver.find_element(locate_with(By.XPATH, "//span[@class='author']")).below({By.XPATH: "//span[@class='js-bned-item-name-text']"})
# wrkRnd = driver.find_element(By.XPATH, "//span[@class='bned-capitalize']")
driver.execute_script("arguments[0].scrollIntoView();", wrkRnd)
webdriver.ActionChains(driver).click(wrkRnd).perform()

chkOut = driver.find_element(By.XPATH, "//button[@alt='Proceed To Cart' ]")
webdriver.ActionChains(driver).click(chkOut).perform()

# copy title off book and enter in google search 


bookLnk = driver.find_element(By.XPATH, "//a[@role='link']").text


time.sleep(2)

driver.switch_to.new_window('tab')
driver.get('https://www.google.com')

Googul = driver.find_element(By.NAME, 'q')
webdriver.ActionChains(driver).click(Googul).perform()
time.sleep(2)
webdriver.ActionChains(driver).send_keys(bookLnk + ' pdf download').perform()
time.sleep(1)
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()



