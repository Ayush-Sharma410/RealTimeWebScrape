from googlesearch import search
import requests
from bs4 import BeautifulSoup
import random
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


def tata1mg(url,pincode):
    driver_path = r'C:\Users\never\OneDrive\Documents\win32\chromedriver_win32'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    action = ActionChains(driver)
    driver.get(url)
    cancel_button= driver.find_element(By.XPATH, '//*[@id="update-city-modal"]/div/div[3]/div[1]')
    cancel_button.click()
    sub_button = driver.find_element(By.XPATH, '//*[@id="eta-content"]/div/div[2]/div[2]/span[1]')
    sub_button.click()
    # Find and fill the form fields
    driver.implicitly_wait(20)
    element1 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[5]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/input')
    element1.send_keys(pincode)
    driver.implicitly_wait(10)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(2)
    title= driver.find_element(By.XPATH,'//*[@id="drug_header"]/div/div/div[1]/div/div[1]/h1')
    Real_price= driver.find_element(By.XPATH,'//*[@id="atc-content"]/div/div[2]/div[1]/div[1]/div[2]/span[2]')
    Discounted_price= driver.find_element(By.XPATH,'//*[@id="atc-content"]/div/div[2]/div[1]/div[1]/div[2]/span[1]')
    Manufacturer= driver.find_element(By.XPATH,'//*[@id="drug_header"]/div/div/div[2]/div[1]/div/div[1]/div[2]')
    Salt= driver.find_element(By.XPATH,'//*[@id="drug_header"]/div/div/div[2]/div[1]/div/div[2]/div[2]')
    Delivery_time = driver.find_element(By.XPATH,'//*[@id="eta-content"]/div/div[1]')
    print("TATA1MG:\n" + title.text+"\n"+Real_price.text+"\n"+Discounted_price.text+"\n"+Manufacturer.text+"\n"+Salt.text+"\n"+Delivery_time.text)

    # Close the web driver
    driver.quit()

def pharmeasy(url,pincode):
    driver_path = r'C:\Users\never\OneDrive\Documents\win32\chromedriver_win32'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    action = ActionChains(driver)
    driver.get(url)
    sub_button = driver.find_element(By.CLASS_NAME, 'PincodeTrigger_pinDetailsText__2M8UP')
    sub_button.click()
    # Find and fill the form fields
    driver.implicitly_wait(10)
    element1 = driver.find_element(By.XPATH, '//*[@id="drawers-portal"]/div/div[2]/div[2]/div[1]/div[2]/div/div/input')
    element1.send_keys(pincode)
    driver.implicitly_wait(10)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(2)
    title= driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/h1')
    Real_price= driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div')
    Discounted_price= driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div/span[1]')
    Manufacturer= driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]')
    Salt= driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[1]/div[5]/div[2]/table/tbody/tr[3]/td[2]')
    Delivery_time = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[4]/div[3]/div/span')
    print("PHARMEASY:\n " + title.text+"\n"+Real_price.text+"\n"+Discounted_price.text+"\n"+Manufacturer.text+"\n"+Salt.text+"\n"+Delivery_time.text)
    driver.quit()

def RealTimeScrape(name,pincode):
    print(f"Searching for {name} ...")
    search_results = list(search(f"{name}", tld="co.in", num=5, lang="en", country="IN", pause=5, stop=5, user_agent='Mozilla/5.0'))
    
    for url in search_results:
        if '1mg.com' in url:
            print(url)
            tata1mg(url,pincode)
        if 'pharmeasy.in' in url:
            print(url)
            pharmeasy(url,pincode)    
name=input("enter the name of the medicine: ")
pincode=int(input("enter your pincode: "))
RealTimeScrape(name,pincode)

