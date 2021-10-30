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
# button = driver.find_element(By.NAME, 'sumbit_doctorSpeField')
# driver.execute_script("arguments[0].click();", button)
# time.sleep(2)
# result = driver.find_elements(By.XPATH, '/html/body/div[2]/section/div/div/table/thead/tr')
# print(len(result))
driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[1]/button').click()
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/ul/li[2]/button').click()
# driver.implicitly_wait(3)
time.sleep(2)
tag = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/tags/span')
# driver.implicitly_wait(3)
time.sleep(2)

tag.clear()
# tag.click()
# driver.implicitly_wait(3)
time.sleep(3)
tag.send_keys('Feeling sad or down')
# driver.implicitly_wait(3)
time.sleep(2)
submit = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div/button')
driver.execute_script("arguments[0].click();", submit)

driver.close()
