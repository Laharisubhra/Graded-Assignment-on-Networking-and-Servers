import os
import requests
import time
import prettytable
from datetime import datetime

# Check the status of the website
def check_status(website):
    try:
        request = requests.get(website)
        return request.status_code
    except requests.ConnectionError:
        return 'Website is down!'

# Check the status of the subdomains every minute
def check_subdomains():
    subdomains = get_subdomains()
    while True:
        clear()
        table = prettytable.PrettyTable(['Subdomain', 'Status'])
        for subdomain in subdomains:
            status = check_status(subdomain)
            table.add_row([subdomain, status])
        print(table)
        time.sleep(60)

# Get the list of subdomains from the text file
def get_subdomains():
    subdomains = []
    with open('subdomains.txt', 'r') as file:
        for line in file:
            subdomains.append(line.strip())
    return subdomains

# Clear the console screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    check_subdomains()