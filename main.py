import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# TODO Be able to add necessary arguments
# TODO Access the sneakers website using selenium
# TODO Find a way to get multiple phone numbers
# TODO Get multiple emails
# TODO Get different forms of payment
# TODO Have program make 'Jigged' addresses
# TODO Change IP addresses - Already have code for this
# TODO Find raffle time

service = Service(executable_path='chromedriver')
driver = webdriver.Chrome(service=service)

URL = "https://www.nike.com/gb/launch"

parser = argparse.ArgumentParser(
    prog='Sneaky Bot',
    description='Bot that will buy sneakers for you',
    epilog='...'
)

parser.add_argument('--username', '-usr', required=True)
parser.add_argument('--password', '-psw', required=True)

args = parser.parse_args()
print(args.accumulate(args.integers))

