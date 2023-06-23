from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Set up Selenium web driver
driver_path = r'C:\Users\never\OneDrive\Documents\win32\chromedriver_win32'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)
# Navigate to the website
driver.get('https://www.1mg.com/drugs/calpol-500mg-tablet-69656')

cancel_button= driver.find_element(By.XPATH, '//*[@id="update-city-modal"]/div/div[3]/div[1]')
cancel_button.click()
print("123")
sub_button = driver.find_element(By.XPATH, '//*[@id="eta-content"]/div/div[2]/div[2]/span[1]')
sub_button.click()
# Find and fill the form fields
driver.implicitly_wait(20)
print("hey")

print("HE")
element1 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[5]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/input')
element1.send_keys('494444')
print("160062")
driver.implicitly_wait(8)

action.send_keys(Keys.ENTER)
action.perform()
# Wait for the page to load after form submission
wait = WebDriverWait(driver, 10)


# Scrape elements from the loaded page
soup = BeautifulSoup(driver.page_source, 'html.parser')

result = driver.find_element(By.XPATH,'//*[@id="eta-content"]/div/div[1]')
print(result.text)

# Close the web driver
driver.quit()