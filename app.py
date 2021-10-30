from TestClass import Test

url = 'http://127.0.0.1:8000/'
test = Test(url=url)
# Landing page status
test.landingHomePage()
# Search  doctor based on city and name
test.test_case_2(city='Dhaka', name='Dr. Abdul Mannan Sarker')
# Search  doctor based only city
test.test_case_3(city='Dhaka')
# Search  doctor based only name
test.test_case_4(name='Dr. Abdul Mannan Sarker')
# Search  hospital based on city and name
test.test_case_5(hospital_name='AFMC - Armed Forces Medical College', city='Dhaka')
# Search  hospital based on city
test.test_case_6(city='Dhaka')
# Search  hospital based on name
test.test_case_7(hospital_name='AFMC - Armed Forces Medical College')
# Show all doctors list
test.test_case_8()
# Show all hospitals list
test.test_case_9()
# Show doctor profile of specific name
test.test_case_10(doctor_name='Dr. Abdul Mannan Sarker')
# Show hospital profile of specific name
test.test_case_11(hospital_name='AFMC - Armed Forces Medical College')
# Go to Covid-19 page and show IEDCR data
test.test_case_12()
# Go to Covid-19 page and show World data
test.test_case_13()
# Sign up a new user
user_info = {
    "first_name": "Ashraful",
    "last_name": "Haque",
    "username": "Ashraf",
    "email": "ashraf01@gmail.com",
    "phone": "01888",
    "Password1": "ashraf",
    "Password2": "ashraf",
    "image": "C:\\Users\\Asus\\Desktop\\default.jpg"
}
test.test_case_14(user_info=user_info)
# Login an user
user_info = {
    "first_name": "Ashraful",
    "username": "Ashraf",
    "Password": "ashraf",
}
test.test_case_15(user_info=user_info)
# Heart Checkup
data = {
    "username": "Ashraf",
    "Password": "ashraf",
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
test.test_case_16(data)
test.generate_report()
