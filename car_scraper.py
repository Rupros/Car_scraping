from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random #for random waiting times

wait_time = [2, 3]
random.seed(6)
def get_random_wait_time():
    return 0.5 +  wait_time[random.randint(0, 1)] * random.random()

options = Options()
 
driver = webdriver.Firefox(options=options)

def is_a_likeable_model(model):
    return model == 'A3' or model == 'A4' or model == 'A5' or model == 'A6'

def header_contains_model(model):
    return 'A3' in model or 'A4' in model or 'A5' in model or 'A6' in model

def load_page():
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except TimeoutException:
        print("Timed out waiting for page to load")

#PARAMS
dealer_max_price = 25000
max_mileage = 150 # in thousands

# links to cars I would be interested in
links = []

# read data from web
url = "https://www.ss.lv/"
driver.get(url)
load_page()

time.sleep(get_random_wait_time())

# go to cars
driver.find_element(By.ID, "mtd_97").click()
load_page()

time.sleep(get_random_wait_time())

# go to Audi
driver.find_element(By.ID, "ahc_103").click()
load_page()

time.sleep(get_random_wait_time())

# enter search params
driver.find_element(By.ID, "f_o_8_min").send_keys(10000)

time.sleep(get_random_wait_time())

driver.find_element(By.ID, "f_o_8_max").send_keys(18000)

time.sleep(get_random_wait_time())

min_year = driver.find_element(By.ID, "f_o_18_min")
min_year.click()
min_year.find_element(By.CSS_SELECTOR, "option[value='2014']").click()

time.sleep(get_random_wait_time())

min_vol = driver.find_element(By.ID, "f_o_15_min")
min_vol.click()
min_vol.find_element(By.CSS_SELECTOR, "option[value='2.0']").click()

time.sleep(get_random_wait_time())

gearbox = driver.find_element(By.ID, "f_o_35")
gearbox.click()
gearbox.find_element(By.CSS_SELECTOR, "option[value='497']").click()

time.sleep(get_random_wait_time())

# sort by mileage
driver.find_element(By.CSS_SELECTOR, "#head_line td:nth-child(5) a").click()
load_page()


has_cars_to_look_at = True
while has_cars_to_look_at:
    time.sleep(get_random_wait_time())
    cars_in_page = driver.find_elements(By.CSS_SELECTOR, "#filter_frm > table:not([id]):not([class]) tbody > tr[id]:not(:first-child)")

    for car in cars_in_page:
        model = car.find_element(By.CSS_SELECTOR, ".msga2-o.pp6 > a")
        mileage_text = car.find_element(By.CSS_SELECTOR, ".msga2-r.pp6 > a").get_attribute("text").split(" ")[0].split(".")[0]
        mileage = int(mileage_text)
        

        if(mileage > max_mileage):
            has_cars_to_look_at = False
            break

        if(is_a_likeable_model(model.get_attribute("text"))):
            link = model.get_attribute("href")
            links.append(link)
    
    next_button = driver.find_element(By.CSS_SELECTOR, '.navi:last-child')
    if("page" not in next_button.get_attribute("href")):
        has_cars_to_look_at = False
    else:
        next_button.click()
        load_page()


url = "https://mollerauto.lv/lv/"
driver.get(url)
load_page()

time.sleep(get_random_wait_time())

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".GdprCookiesPopup-Allow.Button")))
driver.find_element(By.CSS_SELECTOR, ".GdprCookiesPopup-Allow.Button").click()

time.sleep(get_random_wait_time())

# go to Audi
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".GdprCookiesPopup-Allow.Button")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".HomePage-Cards.HomePage-Section .pagebuilder-column-group > div:first-child a")))

goToAudi = driver.find_element(By.CSS_SELECTOR, ".HomePage-Cards.HomePage-Section .pagebuilder-column-group > div:first-child a")
driver.execute_script("arguments[0].scrollIntoView();", goToAudi)
time.sleep(get_random_wait_time())
goToAudi.click()

time.sleep(get_random_wait_time())
load_page()

# sort by price rising
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".FieldSelect-Clickable")))
driver.find_element(By.CSS_SELECTOR, ".FieldSelect-Clickable").click()

time.sleep(get_random_wait_time())

driver.find_element(By.ID, "oASC price").click()

time.sleep(get_random_wait_time())

load_page()

# sort options
time.sleep(get_random_wait_time())
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ExpandableContent.ProductConfigurableAttributes-Expandable")))
driver.find_elements(By.CSS_SELECTOR, ".ExpandableContent.ProductConfigurableAttributes-Expandable")[5].click()
time.sleep(get_random_wait_time())

quattro = driver.find_element(By.CSS_SELECTOR, "#pilnpiedziņa")
driver.execute_script("arguments[0].scrollIntoView();", quattro)
time.sleep(get_random_wait_time())
quattro.click()

load_page()

time.sleep(get_random_wait_time())

header = driver.find_element(By.CSS_SELECTOR, ".Header-Wrapper")
driver.execute_script("arguments[0].remove();", header)

has_cars_to_look_at = True
looked_at_cars = []
while has_cars_to_look_at:
    time.sleep(get_random_wait_time())
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".ProductCard-Link")))
    cars_in_page = driver.find_elements(By.CSS_SELECTOR, ".ProductCard-Link")

    for car in cars_in_page:
        if(car in looked_at_cars):
            continue

        looked_at_cars.append(car)

        model = car.find_element(By.CSS_SELECTOR, ".ProductCard-Name")
        mileage_text = car.find_elements(By.CSS_SELECTOR, ".ProductCard-Link .ProductCard-AdditionalInfo > p")[1].get_attribute("textContent")[:-2].replace(" ", "")
        mileage = int(mileage_text)

        price_text = car.find_element(By.CSS_SELECTOR, ".ProductPrice-PriceValue").get_attribute("textContent")[1:].replace(",", "")[:-3]
        price = int(price_text)
        
        if(price > dealer_max_price):
            has_cars_to_look_at = False
            break

        if(header_contains_model(model.get_attribute("textContent")) and mileage < max_mileage * 1000):
            link = car.get_attribute("href")
            links.append(link)
    
    next_button = driver.find_elements(By.CSS_SELECTOR, '.ProductList-LoadMoreButton')
    if len(next_button) == 0:
        has_cars_to_look_at = False
    else:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", next_button[0])
        time.sleep(get_random_wait_time())
        next_button[0].click()
        load_page()

time.sleep(get_random_wait_time())

# close and print all links to visit
driver.close()

text = ""
for link in links:
    text += link + "\n"

# save in file
f = open("links.txt", "w")
f.write(text)
f.close()
