import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('http://127.0.0.1:8000/users/login/')
driver.find_element(By.NAME, 'email').send_keys('rifat')
driver.find_element(By.NAME, 'password').send_keys('rifat1234')
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[5]/button').click()
driver.find_element(By.LINK_TEXT, 'Check Heart Condition').click()
time.sleep(1)
# Selecting Gender Dropdown menu
select = Select(driver.find_element(By.NAME, 'gender'))
select.select_by_value('0')
# Age
driver.find_element(By.NAME, 'age_1').send_keys(100)
# Fasting blood sugar Radio button
value = '0'
css = "input[value='"+value+"'][name='fbs']"
# driver.find_element(By.CSS_SELECTOR, "input[value='1'][name='fbs']").click()
driver.find_element(By.CSS_SELECTOR, css).click()
# Exercise induced angina
value = '0'
css = "input[value='"+value+"'][name='exang']"
driver.find_element(By.CSS_SELECTOR, css).click()
# Resting electrocardiographic results
select = Select(driver.find_element(By.XPATH, "//select[@name='restecg']"))
select.select_by_value('1')
# Resting blood pressure
driver.find_element(By.NAME, 'trestbps').send_keys(120)
# Chest pain type
select = Select(driver.find_element(By.XPATH, "//select[@name='cp']"))
select.select_by_value('3')
# Heart rate achieved
driver.find_element(By.NAME, 'thalach').send_keys(20)
# Blood disorder (Thalassemia)
select = Select(driver.find_element(By.XPATH, "//select[@name='thal']"))
select.select_by_value('1')
# Slope of peak exercise ST segment
value = '2'
css = "input[value='"+value+"'][name='slope']"
radio = driver.find_element(By.CSS_SELECTOR, css)
driver.execute_script("arguments[0].click();", radio)
# Major vessels (0-3) colored by fluoroscopy
value = '1'
css = "input[value='"+value+"'][name='ca']"
radio = driver.find_element(By.CSS_SELECTOR, css)
driver.execute_script("arguments[0].click();", radio)
# Cholesterol measurement
driver.find_element(By.NAME, 'chol').send_keys(20)
# ST depression induced by exercise relative to rest
driver.find_element(By.NAME, 'oldpeak').send_keys(20)
time.sleep(2)
driver.close()

data = {
    'gender': '1',
    'age': '37',
    'Fasting blood sugar(FBS)': '0',
    'Exercise induced angina': '0',
    'Resting electrocardiographic results': '1',
    'Resting blood pressure': '130',
    'Chest pain type': '2',
    'Heart rate achieved': '187',
    'Blood disorder (Thalassemia)': '2',
    'Slope of peak exercise ST segment': '0',
    'Major vessels (0-3) colored by fluoroscopy': '0',
    'Cholesterol measurement': '250',
    'ST depression induced by exercise relative to rest': '3'
}