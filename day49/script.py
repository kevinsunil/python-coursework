from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_webdriver_path=r"C:\Users\kevin\Desktop\Projects\Python\Development\chromedriver.exe"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3509903625&f_AL=true&f_E=1&f_WT=2&geoId=102713980&keywords=software%20engineer&location=India&refresh=true"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_webdriver_path,options=option)
driver.get(URL)
driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]").click()
time.sleep(5)
username = driver.find_element(By.ID,"username")
username.send_keys("username")
password = driver.find_element(By.ID,"password")
password.send_keys("password")
driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(5)
all_jobs = driver.find_element(By.CSS_SELECTOR,".job-card-container--clickable")
for job in all_jobs:
    try:
        driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button").click()
        driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button").click()
        driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]").click()
        driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]").click()
    
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("Application closed, skipped")
        continue

time.sleep(2)
driver.quit()
