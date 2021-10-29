from TestClass import Test

url = 'http://127.0.0.1:8000/'
test = Test(url=url)
# # Landing page status
# test.landingHomePage()
# # Search  doctor based on city and name
# test.test_case_2(city='Dhaka', name='Dr. Abdul Mannan Sarker')
# # Search  doctor based only city
# test.test_case_3(city='Dhaka')
# # Search  doctor based only name
# test.test_case_4(name='Dr. Abdul Mannan Sarker')
# # Search  hospital based on city and name
# test.test_case_5(hospital_name='AFMC - Armed Forces Medical College', city='Dhaka')
# # Search  hospital based on city
# test.test_case_6(city='Dhaka')
# # Search  hospital based on name
# test.test_case_7(hospital_name='AFMC - Armed Forces Medical College')
test.generate_report()
