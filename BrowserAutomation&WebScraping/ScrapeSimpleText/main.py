from selenium import webdriver

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
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def main():
    driver = create_driver()
    element = driver.find_element("xpath", "/html/body/div[1]/div/h1[1]")
    return element.text

print(main())