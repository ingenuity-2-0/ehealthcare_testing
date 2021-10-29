import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Test:
    report = Report()
    s = Service("./chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    report.setup(
        report_folder=r'Reports',
        module_name='Report',
        release_name='Release 1',
        selenium_driver=driver
    )

    def __init__(self, url):
        self.url = url

    def landingHomePage(self):
        try:
            # Start of Test
            self.report.write_step(
                'Home Page Loading',
                status=self.report.status.Start,
                test_number=1
            )
            time.sleep(2)
            self.driver.get(self.url)
            assert (self.driver.title == 'Home | E-Health Care')
            self.report.write_step(
                'Perfectly landing in the home page',
                status=self.report.status.Pass,
                screenshot=True
            )
        except AssertionError:
            self.report.write_step(
                'Perfectly not landing in the home page',
                status=self.report.status.Fail,
                screenshot=True
            )
        except Exception as e:
            self.report.write_step(
                f'Something went wrong during execution!</br>{e}',
                status=self.report.status.Warn,
                screenshot=True
            )

    def test_case_2(self, city, name):
        try:
            # Start of Test
            self.report.write_step(
                'Search  doctor based on city and name',
                status=self.report.status.Start,
                test_number=2
            )
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[1]/button').click()
            self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/ul/li[1]/button').click()
            self.driver.find_element(By.ID, 'cityField').send_keys(city)
            self.driver.find_element(By.ID, 'doctorSpeField').send_keys(name)
            button = self.driver.find_element(By.XPATH, '//*[@id="pills-appointment"]/div/div[1]/form/button')
            self.driver.execute_script("arguments[0].click();", button)
            r_name = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[1]/a').text
            r_city = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[3]').text

            assert ((r_name == name) and (r_city == city))
            self.report.write_step(
                'Search  doctor matched on city and name',
                status=self.report.status.Pass,
                screenshot=True
            )
        except AssertionError:
            self.report.write_step(
                'Search  doctor not matched on city and name',
                status=self.report.status.Fail,
                screenshot=True
            )
        except Exception as e:
            self.report.write_step(
                f'Something went wrong during execution!</br>{e}',
                status=self.report.status.Warn,
                screenshot=True
            )

    def test_case_3(self, city):
        try:
            self.report.write_step(
                'Search  doctor based only city',
                status=self.report.status.Start,
                test_number=3
            )
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[1]/button').click()
            self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/ul/li[1]/button').click()
            self.driver.find_element(By.ID, 'cityField').send_keys(city)
            button = self.driver.find_element(By.XPATH, '//*[@id="pills-appointment"]/div/div[1]/form/button')
            self.driver.execute_script("arguments[0].click();", button)
            r_city = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[3]').text

            assert (r_city == city)
            self.report.write_step(
                'Search  doctor matched on',
                status=self.report.status.Pass,
                screenshot=True
            )
        except AssertionError:
            self.report.write_step(
                'Search  doctor not matched on city',
                status=self.report.status.Fail,
                screenshot=True
            )
        except Exception as e:
            self.report.write_step(
                f'Something went wrong during execution!</br>{e}',
                status=self.report.status.Warn,
                screenshot=True
            )

    def test_case_4(self, name):
        try:
            self.report.write_step(
                'Search  doctor based on name',
                status=self.report.status.Start,
                test_number=4
            )
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[1]/button').click()
            self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/ul/li[1]/button').click()
            self.driver.find_element(By.ID, 'doctorSpeField').send_keys(name)
            button = self.driver.find_element(By.XPATH, '//*[@id="pills-appointment"]/div/div[1]/form/button')
            self.driver.execute_script("arguments[0].click();", button)
            r_name = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[1]/a').text

            assert (r_name == name)
            self.report.write_step(
                'Search  doctor matched on name',
                status=self.report.status.Pass,
                screenshot=True
            )
        except AssertionError:
            self.report.write_step(
                'Search  doctor not matched on name',
                status=self.report.status.Fail,
                screenshot=True
            )
        except Exception as e:
            self.report.write_step(
                f'Something went wrong during execution!</br>{e}',
                status=self.report.status.Warn,
                screenshot=True
            )

    def test_case_5(self, city, hospital_name):
        try:
            # Start of Test
            self.report.write_step(
                'Search  Hospital based on city and name',
                status=self.report.status.Start,
                test_number=5
            )
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[2]/button').click()
            self.driver.implicitly_wait(1)
            self.driver.find_element(By.ID, 'cityField2').send_keys(city)
            self.driver.find_element(By.ID, 'hospitalField').send_keys(hospital_name)
            button = self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[2]/div/div[1]/form/button')
            self.driver.execute_script("arguments[0].click();", button)
            r_name = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[1]/a').text
            r_city = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[3]').text

            assert ((r_name == hospital_name) and (r_city == city))
            self.report.write_step(
                'Search hospital matched on city and name',
                status=self.report.status.Pass,
                screenshot=True
            )
        except AssertionError:
            self.report.write_step(
                'Search hospital not matched on city and name',
                status=self.report.status.Fail,
                screenshot=True
            )
        except Exception as e:
            self.report.write_step(
                f'Something went wrong during execution!</br>{e}',
                status=self.report.status.Warn,
                screenshot=True
            )

    def test_case_6(self, city):
        try:
            self.report.write_step(
                'Search  Hospital based on city',
                status=self.report.status.Start,
                test_number=6
            )
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[2]/button').click()
            self.driver.implicitly_wait(1)
            self.driver.find_element(By.ID, 'cityField2').send_keys(city)
            button = self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[2]/div/div[1]/form/button')
            self.driver.execute_script("arguments[0].click();", button)
            r_city = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[3]').text

            assert (r_city == city)
            self.report.write_step(
                'Search hospital matched on city',
                status=self.report.status.Pass,
                screenshot=True
            )
        except AssertionError:
            self.report.write_step(
                'Search hospital not matched on city',
                status=self.report.status.Fail,
                screenshot=True
            )
        except Exception as e:
            self.report.write_step(
                f'Something went wrong during execution!</br>{e}',
                status=self.report.status.Warn,
                screenshot=True
            )

    def test_case_7(self, hospital_name):
        try:
            self.report.write_step(
                'Search  Hospital based on name',
                status=self.report.status.Start,
                test_number=7
            )
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/div/ul/li[2]/button').click()
            self.driver.implicitly_wait(1)
            self.driver.find_element(By.ID, 'hospitalField').send_keys(hospital_name)
            button = self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div/div[2]/div/div[1]/form/button')
            self.driver.execute_script("arguments[0].click();", button)
            r_name = self.driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[1]/a').text

            assert (r_name == hospital_name)
            self.report.write_step(
                'Search hospital matched on name',
                status=self.report.status.Pass,
                screenshot=True
            )
        except AssertionError:
            self.report.write_step(
                'Search hospital not matched on name',
                status=self.report.status.Fail,
                screenshot=True
            )
        except Exception as e:
            self.report.write_step(
                f'Something went wrong during execution!</br>{e}',
                status=self.report.status.Warn,
                screenshot=True
            )

    def generate_report(self):
        self.report.generate_report()
        self.driver.quit()
