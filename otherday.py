from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date
from datetime import timedelta
import time
import sys

# Any dates listed after the function is called is put into this list called days
days = sys.argv[1:]

# Here, you can double check your date inputs
print(days)

# URL to scrape
url = "https://www.nyse.com/regulation/threshold-securities"

# Using the datetime library to calculate yesterday's date
today = date.today()
yesterday = today - timedelta(days = 1)
formatted_yest = yesterday.strftime('%m/%d/%Y')

# Starting Google Chrome and opening the URL given above
driver = webdriver.Chrome()
driver.get(url)

# Wait for the section we need to load
# If more than 30 seconds passes and the site still isn't done loading, an error is thrown
# The input box should have yesterday's date in it since it's the most recent data
WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element_value((By.ID, "selectedDate"), f'{yesterday}'))

# For each of our input dates...
for day in days:
    # no cleaning needed since Python accepts all command line args as strings and we need a string

    # the date is entered into the date input box
    enter_date = driver.find_element('id', 'selectedDate')
    enter_date.send_keys(f'{day}')

    time.sleep(1) # brief wait to make sure we aren't moving too fast

    # the download button is clicked and the .txt file goes straight to the Downloads folder
    download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div[4]/a[span]").click()

# A 5 second wait to make sure the downloads start
# (the code to wait until your computer is done downloading was a little sketchy to me so I went for an explicit wait instead)
time.sleep(5)

# Close this one Chrome window (will not interfere with others)
driver.close()