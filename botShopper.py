from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
import time


print("Welcome to BotShopper!, please select from our options of sites to shop from")
print("1.Amazon \n2.Kroger \n3.Gamestop")
selection = int(input())
    
if selection == 1:

     product = str(input("Please enter the name of the product you wish to purchase: "))
     driver = webdriver.Safari()
     driver.get('https://www.amazon.com')
     time.sleep(1)
     driver.fullscreen_window()
     srch = driver.find_element(By.XPATH, "//input[@type='text']")
     webdriver.ActionChains(driver).click(srch).send_keys(product).send_keys(Keys.ENTER).perform()
     time.sleep(3)
     
     
     
elif selection == 2:

        item = str(input("Please enter the item you wish to purchase: "))
        user = str(input("Enter your email for site login: "))
        psswrd = str(input("Please enter your password as well: "))
        driver = webdriver.Safari()
        driver.get('https://www.kroger.com/signin?redirectUrl=/search%3Fquery%3Dbar%26searchType%3Ddefault_search')
        time.sleep(1)
        driver.fullscreen_window()       
        time.sleep(1)

        popUp = driver.find_element(By.XPATH, "//button[@aria-label='Close pop-up']")
        webdriver.ActionChains(driver).click(popUp).perform()
        time.sleep(1)

        ntrEml = driver.find_element(By.XPATH, "//input[@type='email']")
        webdriver.ActionChains(driver).click(ntrEml).send_keys(user).perform()
        time.sleep(1)
        
        ntrPswrd = driver.find_element(By.XPATH, "//input[@type='password']")
        webdriver.ActionChains(driver).click(ntrPswrd).send_keys(psswrd).perform()

        time.sleep(1)
        sgnIn = driver.find_element(By.XPATH, "//button[@type='submit']")
        webdriver.ActionChains(driver).click(sgnIn).perform()
        time.sleep(2)

        if driver.find_element(By.XPATH, "//span[@class='kds-Text--s kds-Message-content']"):
            webdriver.ActionChains(driver).click(sgnIn).perform()
            time.sleep(1)
            webdriver.ActionChains(driver).click(sgnIn).perform()
            time.sleep(1)
            webdriver.ActionChains(driver).click(sgnIn).perform()
            time.sleep(1)
            webdriver.ActionChains(driver).click(sgnIn).perform()

        else:
            pass


        # srchBar = driver.find_element(By.XPATH, "//input[@type='search']")
        # webdriver.ActionChains(driver).click(srchBar).send_keys(item).send_keys(Keys.ENTER).perform()

elif selection == 3:

    game = str(input("Enter the game, console, or accesory you wanna buy: "))
    driver = webdriver.Safari()
    driver.get('https://www.gamestop.com')
    time.sleep(1)
    driver.fullscreen_window()
    time.sleep(4)
    inp = driver.find_element(By.XPATH, "//input[@name='q']")
    webdriver.ActionChains(driver).click(inp).send_keys(game).perform()
    time.sleep(1)
    webdriver.ActionChains(driver).click(inp).send_keys(Keys.ENTER).perform()
        
