from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Set up Selenium web driver
driver_path = r'C:\Users\never\OneDrive\Documents\win32\chromedriver_win32'
service = Service(driver_path)
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)
# Navigate to the website
driver.get('https://pharmeasy.in/online-medicine-order/calpol-500mg-strip-of-15-tablets-38810')

sub_button = driver.find_element(By.CLASS_NAME, 'PincodeTrigger_pinDetailsText__2M8UP')
sub_button.click()
# Find and fill the form fields
driver.implicitly_wait(10)
element1 = driver.find_element(By.XPATH, '//*[@id="drawers-portal"]/div/div[2]/div[2]/div[1]/div[2]/div/div/input')
element1.send_keys('494444')
print("160062")
driver.implicitly_wait(8)

action.send_keys(Keys.ENTER)
action.perform()
# Wait for the page to load after form submission
wait = WebDriverWait(driver, 10)




result = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[4]/div[3]/div/span')
print(result.text)

# Close the web driver
driver.quit()