from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def create_driver():
    # Set options for the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('dissable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get("https://online.uom.lk/login/index.php")
    return driver

def main():
    driver = create_driver()
    driver.find_element("id", "username").send_keys("<your_username>")
    driver.find_element("id","password").send_keys("<your_password>" + Keys.RETURN)
    sleep(2)
    print(driver.current_url)

print(main()) 