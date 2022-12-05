from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
from datetime import timedelta
import time

# URL to scrape
url = "https://www.nyse.com/regulation/threshold-securities"

# Using the datetime library to calculate yesterday's date
today = date.today()
yesterday = today - timedelta(days = 1)
formatted_yest = yesterday.strftime('%m/%d/%Y')

# Starting Google Chrome and opening the URL given above
driver = webdriver.Chrome()
driver.get(url)

time.sleep(1) # brief wait to make sure we aren't moving too fast

# the download button is clicked and the .txt file goes straight to the Downloads folder
download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div[4]/a[span]").click()

# A 5 second wait to make sure the downloads start
# (the code to wait until your computer is done downloading was a little sketchy to me so I went for an explicit wait instead)
time.sleep(5) 

# Close this one Chrome window (will not interfere with others)
driver.close()

