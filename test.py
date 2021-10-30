import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('http://127.0.0.1:8000')
driver.find_element(By.XPATH, '/html/body/div/div/nav/div/div/a[1]/button').click()
driver.find_element(By.NAME, 'email').send_keys('rifat')
driver.find_element(By.NAME, 'password').send_keys('rifat1234')
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[5]/button').click()

driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div/nav/div/div/div/ul/li[3]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div/div/div/div/div/div/div[2]/a/button').click()
time.sleep(2)

# submit = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div/button')
# driver.execute_script("arguments[0].click();", submit)

driver.close()
