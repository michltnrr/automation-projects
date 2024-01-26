from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import NoSuchElementException

import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_data():
    person = input("Enter persons roblox username: ")
    user_bloxname = input("Enter your roblox username for login: ")
    user_bloxpsrd = input("Enter your password: ")
    user_email = input("Enter your email: ")

    # new_target = 'cheezyyz1'
    # person = 'nbhd511'
    # user_bloxname = 'blackrpatz'
    # user_bloxpsrd = 'robloxislife'
    # user_email = 'michaeldturner21@gmail.com'

    driver = webdriver.Safari()

    driver.get(f"https://www.roblox.com/search/users?keyword={person}")
    time.sleep(1)
    driver.fullscreen_window()
    time.sleep(2)
    signIn = driver.find_element(By.LINK_TEXT, "Log In")
    webdriver.ActionChains(driver).click(signIn).perform()

    return driver, person, user_bloxname, user_bloxpsrd, user_email


def login(driver, user_bloxname, user_bloxpsrd):
    time.sleep(1)
    login_btn = driver.find_element(By.ID, 'login-username').send_keys(user_bloxname)
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.TAB).send_keys(user_bloxpsrd).perform()
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()


def locate_victim(driver):
    time.sleep(3)
    accounts = driver.find_elements(By.CLASS_NAME, 'avatar-card-content')
    if accounts:
        target = accounts[0]
        webdriver.ActionChains(driver).click(target).perform()
        time.sleep(3)


# ----------------------------------------------------        check if target is online       --------------------------------------------------------------

def is_online(driver, person, user_email):
    first_check = True
    try:
        if not first_check:
            driver.refresh()
            time.sleep(3)
            """
            may modify to check status even if the target isnt friends w the user
            also want to send an alert when the email has been sent 
            """
        online = driver.find_element(By.CLASS_NAME, 'btn-join-game')
        
        if online:
            email(person, user_email)


    except NoSuchElementException:
        print(f"{person} is currently offline 👎🏽")
        # os.system('clear')
        
    first_check = False

def email(person, user_email):
    #email content
    body = f"{person} is currently online ✅"
    subject = 'bloxstalk player status'
    
    
    #send email
    sender_email = 'michlneuro15@gmail.com'
    sender_pswrd = 'cyfh sqoc rssj owhs'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = user_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server (in this example, using Gmail)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_pswrd)
        text = message.as_string()
        server.sendmail(sender_email, user_email, text)

def main():
    driver, person, user_bloxname, user_bloxpsrd, user_email = get_data()
    login(driver, user_bloxname, user_bloxpsrd)
    locate_victim(driver)
    is_online(driver, person, user_email)
    schedule.every(1).minutes.do(is_online)

    while True:
        schedule.run_pending()
        time.sleep(1)
main()