from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
import time
import os

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


def clean_text(text):
    output = float(text.split(": ")[1])
    return output

def write_file(text):
    """write text to a file"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    saved_files_dir = os.path.join(script_dir, "Saved_files")
    
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    filepath = os.path.join(saved_files_dir, f"login_data_{filename}")
    
    with open(filepath, "w") as f:
        f.write(text)

def main():
    driver = create_driver()
    driver.find_element("id", "id_username").send_keys("automated")
    driver.find_element("id","id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element("xpath", "/html/body/nav/div/a").click()
    print(driver.current_url)
    for i in range(5):
        time.sleep(2)  # Wait for the page to load after login
        element = driver.find_element("xpath", "/html/body/div[1]/div/h1[2]")
        text =  str(clean_text(element.text))
        write_file(text)

main()