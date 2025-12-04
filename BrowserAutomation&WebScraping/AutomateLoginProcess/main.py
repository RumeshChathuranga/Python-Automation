from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = create_driver()
    driver.find_element("id", "id_username").send_keys("automated")
    driver.find_element("id","id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element("xpath", "/html/body/nav/div/a").click()
    print(driver.current_url)

print(main()) 