from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
import time

def initiation():
    
    print("Welcome to BotShopper!, please select from our options of sites to shop from")
    print("1.Amazon \n2.Kroger \n3.Gamestop")
    selection = int(input())
    
    if selection == 1:
        
        product = str(input("Please enter the name of the product you wish to purchase: "))
        driver = webdriver.Safari()
        driver.get('https://www.amazon.com')
        time.sleep(1)
        driver.fullscreen_window()
        # time.sleep(1)
        srch = driver.find_element(By.XPATH, "//input[@type='text']")
        webdriver.ActionChains(driver).click(srch).send_keys(product).send_keys(Keys.ENTER).perform()
     
     
    elif selection == 2:
        
        item = str(input("Please enter the item you wish to purchase: "))
        driver = webdriver.Safari()
        # time.sleep(1)
        driver.get('https://www.kroger.com')
        time.sleep(1)
        driver.fullscreen_window()
        time.sleep(1)
        srchBar = driver.find_element(By.XPATH, "//input[@type='search']")
        webdriver.ActionChains(driver).click(srchBar).send_keys(item).send_keys(Keys.ENTER).perform()

    elif selection == 3:

        game = str(input("Enter the game, console, or accesory you wanna buy: "))
        driver = webdriver.Safari()
        driver.get('https://www.gamestop.com')
        time.sleep(1)
        driver.fullscreen_window()
        time.sleep(2)
        inp = driver.find_element(By.TAG_NAME, 'input')
        webdriver.ActionChains(driver).click(inp).send_keys(game).perform()
        


initiation()
