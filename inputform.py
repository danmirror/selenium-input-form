
import csv
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    driver = webdriver.Chrome()
    for line in csv_reader:
        if(line[0] != "Name"):
            driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeHdfOVeCqd72QgeHww-5Ob85hdGAsuJN-8BEwNhxUyjhrqbw/viewform?usp=sf_link')
            time.sleep(1)
            name_field = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            name_field.send_keys(line[0])
            
            age_field = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            age_field.send_keys(line[1])
            
            score_field = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            score_field.send_keys(line[2])
            
            submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit.click()
            time.sleep(1)
