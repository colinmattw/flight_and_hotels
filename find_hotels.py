from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pyautogui
import re
import csv

driver = webdriver.Chrome()

def price_element(n): 
        return '/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[' + str(n) + ']'

def find_hotel_price(city):

    driver.get('https://www.booking.com/searchresults.html?label=ADxWIPIbjGojii8jlGPKTDg_jkCmXpdC-jqLHQUFhT7tFOoYArFUOYA%3D%3D&aid=2210273&ss=Tokyo&ssne=Tokyo&ssne_untouched=Tokyo&lang=en-us&sb=1&src_elem=sb&dest_id=-246227&dest_type=city&checkin=2023-10-06&checkout=2023-10-14&group_adults=2&no_rooms=1&group_children=0&order=class_and_price')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/form/div[1]/div[1]/div/div/div[1]/div/div/div[3]')))
    x_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/div[1]/div[1]/div/div/div[1]/div/div/div[3]')
    x_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/form/div[1]/div[1]/div/div/div[1]/div/div/input')))
    city_input = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/div[1]/div[1]/div/div/div[1]/div/div/input')
    city_input.send_keys(city)
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/form/div[1]/div[4]/button')))
    x_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/div[1]/div[4]/button')
    x_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[4]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]')))
        chart_element_html = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]').get_attribute("innerHTML")
    except TimeoutException:
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div[4]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]')))
            chart_element_html = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]').get_attribute("innerHTML")
        except TimeoutException:
            return 'None'

    price_bars_matches = re.findall(r'height: (0|[1-9]\d{0,1}|100)%', chart_element_html)
    price_range = str(re.search(r'\$[\d,]+ \u2013 \$[\d,]+', chart_element_html).group(0)).replace('$', '').replace(' ', '').replace(',', '').split('\u2013')
    price_range = (int(price_range[0]), int(price_range[1]), (int(price_range[1]) - int(price_range[0])))
    price_bars_ints = []
    for bar in price_bars_matches:
         price_bars_ints.append(int(bar))
    theoretical_hotels = 0
    for bar in price_bars_ints:
         theoretical_hotels += bar
    total_hotel_price = 0
    price_change_per_bar = (price_range[2] / 50)
    for i, bar in enumerate(price_bars_ints):
         price_at_bar = (i * price_change_per_bar) + price_range[0] + (price_change_per_bar / 2)
         total_hotel_price += bar * price_at_bar

    try:
        avg_price = total_hotel_price / theoretical_hotels
        return(avg_price)
    except ZeroDivisionError:
         return 'None'




cities = []
with open('expanded_cities_list.txt', 'r')  as cities_file:
    with open('city_avg_hotel_price.csv', 'a') as price_file:
        writer = csv.writer(price_file)
        writer.writerow(['City', 'Avg Hotel Price'])
        for i,city in enumerate(cities_file):
            if(i > 163):     
                city_better = city.replace(' ', '').split(',')
                city_better = city_better[1].strip() + ', ' + city_better[0]
                writer.writerow([city_better, find_hotel_price(city_better)])

driver.close()
driver.quit()