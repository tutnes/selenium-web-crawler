# Import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sys
from bs4 import BeautifulSoup

# Define Browser Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Hides the browser window
# Reference the local Chromedriver instance

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# Run the Webdriver, save page an quit browser
driver.get(sys.argv[1])

# imports
import time

# Scroll page to load whole content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to the bottom.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load the page
    time.sleep(2)
    # Calculate new scroll height and compare with last height.
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

htmltext = driver.page_source
# Parse HTML structure
soup = BeautifulSoup(htmltext, "lxml")
# Extract links to profiles from TWDS Authors
links = {}
for link in soup.find_all("a"):
    currentlink = link.get('href')
    if (currentlink):
        if ('https://' or 'http://') in currentlink:
            links[currentlink] = True

print(links)

driver.quit()
