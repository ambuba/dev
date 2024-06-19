from selenium import webdriver
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
    driver.get("http://automated.pythonanywhere.com")
    return driver

# Store dynamic temperature value in a variable
def extract_temp(temp_string):
    """Extract temperature value only from the returned text"""
    temp = float(temp_string.split(": ")[1])
    return temp

def main():
    driver = get_driver()
    #element = driver.find_element("xpath", "/html/body/div[1]/div/h1[1]")
    # Scrap dynamic value
    time.sleep(2)
    element = driver.find_element("xpath", "/html/body/div[1]/div/h1[2]")
    return extract_temp(element.text)

print(main())