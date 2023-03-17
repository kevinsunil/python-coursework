from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\kevin\Desktop\Projects\Python\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
dates = driver.find_elements(By.CLASS_NAME, "event-widget.last time")
date_list = []
for date in dates:
    date_list.append(date.text)
event_name = driver.find_elements(By.CLASS_NAME,"event-widget.last li a")
event_list = []
for event in event_name:
    event_list.append(event.text)
event_details = {}
for i in range (0,len(date_list)):
    event_details[i] = {
        "date": date_list[i],
        "name": event_list[i]
    }
print(event_details)
driver.quit()
