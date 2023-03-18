from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r"C:\Users\kevin\Desktop\Projects\Python\Development\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(chrome_driver_path,options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID,"cookie")
check_time = time.time() + 5
stop_time = time.time() + 60*120

purchase_items = driver.find_elements(By.CLASS_NAME,"grayed")
purchase_items.pop()
item_list = [item.get_attribute("id") for item in purchase_items]
game_on = True

while game_on:
    cookie.click()
    if time.time() > check_time:
        store_item = driver.find_elements(By.CSS_SELECTOR,"#store b")
        price_list = []

        for price in store_item:
            item_price = price.text
            if item_price != "":
                actual_price = int(item_price.split("-")[1].strip().replace(",",""))
                price_list.append(actual_price)
        upgrades = {}
        for i in range(len(price_list)):
            upgrades[price_list[i]] = item_list[i]
        cookie_total = driver.find_element(By.ID,"money").text
        if "," in cookie_total:
            cookie_total = cookie_total.replace(",","")
        cookie_total = int(cookie_total)
        buyable_upgrades = {}
        for actual_price,id in upgrades.items():
            if cookie_total > actual_price:
                buyable_upgrades[actual_price] = id
        try:
            max_upgrade = max(buyable_upgrades)
            id_item = buyable_upgrades[max_upgrade]
            driver.find_element(By.ID,id_item).click()
        except:
            pass

        check_time = time.time() +5
    if time.time() > stop_time:
        cps = driver.find_element(By.ID,"cps").text
        print(cps)
        game_on = False


