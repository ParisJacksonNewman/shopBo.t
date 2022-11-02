import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# TODO Be able to add necessary arguments
# TODO Access the sneakers website using selenium
# TODO Find a way to get multiple phone numbers
# TODO Get multiple emails
# TODO Get different forms of payment
# TODO Have program make 'Jigged' addresses
# TODO Change IP addresses - Already have code for this
# TODO Find raffle time

URL = "https://www.nike.com/gb/launch"

def get_args():
    parser = argparse.ArgumentParser(
        prog='Sneaky Bot',
        description='Bot that will buy sneakers for you',
        epilog='...'
    )

    parser.add_argument('--username', '-usr', required=True)
    parser.add_argument('--password', '-psw', required=True)

    args = parser.parse_args()
    
    return args.username, args.password

def login(username, password, url):
    service = Service(executable_path='chromedriver')

    driver = webdriver.Chrome(service=service)

    driver.get(url)

    driver.implicitly_wait(0.5)

    login_button = driver.find_element(by=By.CLASS_NAME, value='join-log-in')

    login_button.click()

    driver.quit()

    #...

username, password = get_args()

print(username)
print(password)

