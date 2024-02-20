import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie= driver.find_element(By.ID,value="cookie")

additoinal_click = driver.find_elements(By.CSS_SELECTOR,value="#store .grayed b")
store = driver.find_elements(By.CLASS_NAME,value="grayed")
new_dict = {}
value = []
item =[]
for product in store:

    key = product.get_attribute("id")
    item.append(key)

i =0

for e in additoinal_click:
    list = e.text.split("-")
    if len(list) > 1:
        cost = list[1].strip(" ")
        value.append(cost.replace(",",""))
        new_dict[f"{item[i]}"] = cost
    i+=1




timeout = time.time()+5
five_min = time.time()+300

while True:

    cookie.click()
    cookie_count = driver.find_element(By.ID,value="money").text
    if time.time()>timeout:

        affordable_items ={}
        for id,cost in new_dict.items():

            if cookie_count>cost:
                affordable_items[cost]=id

        highest_price = max(affordable_items)
        print(highest_price)

        to_purchase_id = affordable_items[highest_price]

        driver.find_element(By.ID,value=to_purchase_id).click()

        timeout =time.time()+5

        if time.time()>five_min:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_s)
            break
