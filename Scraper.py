# import required libraries
import requests
import re
import csv

import row as row
from bs4 import BeautifulSoup

url = input("Please enter the URL (ex. https://pcb.illinois.gov/AboutIPCB/StaffDirectory): ")
emailsList = []

# Requests the page and then soupifies it
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# Use regex to find emails and then add it to the emailsList list
actualEmails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup.text, re.I))
emailsList.append(actualEmails)

print(*actualEmails, sep = "\n")

with open('output.txt', 'w') as f:
    for line in actualEmails:
        f.writelines(line)
        f.writelines('\n')


with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in actualEmails:
        writer.writerows([[i]])
