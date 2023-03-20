from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver_path= r"C:/Users/kevin/Desktop/Projects/Python/Development/chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(executable_path=chrome_driver_path,options=option)
driver.get("https://www.speedtest.net/")
driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div[3]/button").click()
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
time.sleep(65)
download_speed=driver.find_element(By.CLASS_NAME,"download-speed")
upload_speed = driver.find_element(By.CLASS_NAME,"upload-speed")
print(download_speed.text)
print(upload_speed.text)
