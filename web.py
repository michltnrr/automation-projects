from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Safari()

driver.get('https://www.google.com')
 
#finds link to click by its text
searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")

# perfoms a double click
webdriver.ActionChains(driver).double_click(searchBtn).perform()

#locates signin element and complete sing in
email = 'John.Doe@gmail.com'
Singin = driver.find_element(By.NAME, "identifier").send_keys(email + Keys.ENTER)

# retry = driver.find_element(By.LINK_TEXT, "Try again")
# webdriver.ActionChains(driver).double_click(retry).perform()
