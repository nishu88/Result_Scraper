URL = "http://results.rvce.edu.in/viewresult2.php"
# Output file name (in CSV format)
FILENAME = "TE2019_4thSEM.csv"
# Starting USN
USN_START = 1
# Ending USN
USN_END =250
# Year of joining (15 for 2015, 16 for 2016 etc.)
YEAR_OF_JOINING = "17"
# Department (2 letter code: AS, CS, CV, IS, ME etc.)
DEPARTMENT = "TE"
# Print result to console (True or False)
PRINT_TO_CONSOLE = True

###############################################################################

######## Imports ########
# For making POST requests
import requests
# For parsing the html
from bs4 import BeautifulSoup
# For exporting/saving to a CSV file
import csv

###############################################################################

def getCaptcha(session):
    result = session.post(URL)
    soup = BeautifulSoup(result.content, "lxml")
    samples = soup.find_all("label")
    captcha = str(samples[1].string)
    num1 = captcha[8]
    num2 = captcha[12]
    ans = int(num1) + int(num2)
    return ans

###############################################################################

def getResult(session):

    rows = []
    ans = getCaptcha(session)

    for i in range(USN_START, USN_END + 1):

        params = {
            "usn": "1RV" + YEAR_OF_JOINING + DEPARTMENT + '{:03}'.format(i),
            "captcha": ans
        }
        result = session.post(URL, params)

        soup = BeautifulSoup(result.content, "lxml")
        checkVal = soup.find(attrs={"data-title" : "PROGRAMME"})

        # Skip if no result is found
        if checkVal:
            # Extract the required fields
            name = soup.find(attrs={"data-title" : "NAME"}).string
            usn = soup.find(attrs={"data-title" : "USN"}).string
            grades = soup.find_all(attrs={"data-title" : "GRADE"})
            sgpa = soup.find(attrs={"data-title" : "SGPA"}).string

            # Create a row with the details and results of 1 person
            row = []
            row.append(name)
            row.append(usn)
            for grade in grades:
                row.append(grade.string)
            row.append(sgpa)

            # Append to the list
            rows.append(row)
            if (PRINT_TO_CONSOLE):
                print(row)

    return rows

###############################################################################

def writeResult(rows):
    with open(FILENAME, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerows(rows)

###############################################################################

# Create a new session
session = requests.session()
# Time for action
writeResult(getResult(session))
