from selenium import webdriver
import time

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

def clean_text(text):
    output = float(text.split(": ")[1])
    return output



def main():
    driver = create_driver()
    time.sleep(2)  # Wait for the dynamic content to load
    element = driver.find_element("xpath", "/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


print(main())