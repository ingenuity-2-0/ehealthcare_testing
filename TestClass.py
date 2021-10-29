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

    def generate_report(self):
        self.report.generate_report()
        self.driver.quit()
