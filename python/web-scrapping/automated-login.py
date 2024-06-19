from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
    # Set options for easier browsing
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()   
    # Populate username fiedl on the login form with the 'automated' user 
    driver.find_element("id", "id_username").send_keys("automated")
    time.sleep(2)
    # Enter password
    driver.find_element("id", "id_password").send_keys("automatedautomated" + Keys.RETURN)
    # Check where we currently are in the application
    # print(driver.current_url)
    time.sleep(2)
    # Click home button once logged in to navigate to home
    driver.find_element("xpath", "/html/body/nav/div/a").click()
    print(driver.current_url)
    

print(main())