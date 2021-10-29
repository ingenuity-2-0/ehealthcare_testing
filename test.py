# pip install pyhtmlreport
import time

from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

report = Report()
s = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=s)

report.setup(
    report_folder=r'E:\Mehrab\Reports',
    module_name='Report',
    release_name='Release 1',
    selenium_driver=driver
)
driver.get('http://192.168.0.117:8080/')

# Test case 1 Open The project
try:
    # Start of Test
    report.write_step(
        'Home Page Loading',
        status=report.status.Start,
        test_number=1
    )
    # print(driver.title)
    # time.sleep(5)
    assert (driver.title == 'Courses')
    report.write_step(
        'Perfactly landing in the home page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Perfactly not landing in the home page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test case 2 creat a user without error
driver.get('http://192.168.0.117:8080/')
try:
    # Start of Test
    report.write_step(
        'Create a User without error',
        status=report.status.Start,
        test_number=2
    )
    driver.find_element(By.LINK_TEXT, 'Signup').click()
    driver.find_element(By.ID, "id_first_name").send_keys('Sabbir')
    time.sleep(3)
    driver.find_element(By.ID, "id_last_name").send_keys('hosen')
    time.sleep(2)
    driver.find_element(By.ID, "id_username").send_keys('hosen')
    time.sleep(2)
    driver.find_element(By.ID, "id_email").send_keys('hosen@gmail.com')
    time.sleep(2)
    driver.find_element(By.ID, "id_password1").send_keys('cse123456')
    time.sleep(2)
    driver.find_element(By.ID, "id_password2").send_keys('cse123456')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]').click()
    assert driver.title == 'Login'
    report.write_step(
        'User Created',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'User Not created',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
finally:
    report.generate_report()
    driver.quit()
