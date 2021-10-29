import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('http://127.0.0.1:8000')
# driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[1]/button').click()
# driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/ul/li[1]/button').click()
# driver.find_element(By.ID, 'cityField').send_keys('Dhaka')
# driver.find_element(By.ID, 'doctorSpeField').send_keys('Dr. Abdul Mannan Sarker')
# driver.refresh()
# time.sleep(1)

button = driver.find_element(By.NAME, 'sumbit_doctorSpeField')
driver.execute_script("arguments[0].click();", button)
time.sleep(2)
driver.close()
