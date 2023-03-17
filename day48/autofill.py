from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\kevin\Desktop\Projects\Python\Development\chromedriver.exe"


options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(executable_path=chrome_driver_path,options=options)
driver.get(url="https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME,"fName")
first_name.send_keys("Kevin")
last_name = driver.find_element(By.NAME,"lName")
last_name.send_keys("George")
email = driver.find_element(By.NAME,"email")
email.send_keys("example.co@gmail.com")
# submit = driver.find_element(By.LINK_TEXT,"Sign UP")
# submit.click()
