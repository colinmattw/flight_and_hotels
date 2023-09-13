from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pyautogui
import re

# Initialize the Chrome driver

driver = webdriver.Chrome()
    
def shortest_time(time_list):

    times = []
    for i,t in enumerate(time_list):
        exp = re.search(r'(\d+)\s*hr\s*(\d+)\s*min|(\d+)\s*hr|(\d+)\s*min', t)
        times.append(0)
        if(exp.group(1) is not None):
            times[i] += (int(exp.group(1)) * 60)
        if(exp.group(2) is not None):
            times[i] += (int(exp.group(2)))
        if(exp.group(3) is not None):
            times[i] += (int(exp.group(3)) * 60)
        if(exp.group(4) is not None):
            times[i] += (int(exp.group(4)))

    shortest_time =  (6000, 0)
    for i,time in enumerate(times):
        if(time < shortest_time[0]):
            shortest_time = (time, i)
    return time_list[shortest_time[1]]

def cheapest_price(price_list):
    stripped_prices = []
    for price in price_list:
        stripped_prices.append(int(price.replace('$', '').replace(',', '')))
    lowest_price = 99999
    for price in stripped_prices:
        if(price < lowest_price):
            lowest_price = price
    return lowest_price

def get_flight_data(starting_loc, dest):

    # Navigate to a website
    driver.get("https://www.google.com/travel/explore?tfs=CBwQAxoaEgoyMDIzLTEwLTA2agwIAhIIL20vMGZ0eHcaGhIKMjAyMy0xMC0xNHIMCAISCC9tLzBmdHh3QAFIAXABggELCP___________wGYAQGyAQQYASAB&tfu=GgA")

    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/div/input')))
    from_input = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/div/input')
    from_input.clear()
    from_input.send_keys(starting_loc)
    time.sleep(0.25)
    pyautogui.press('down')
    time.sleep(0.25)
    pyautogui.press('down')
    time.sleep(0.25)
    pyautogui.press('enter')


    time.sleep(0.25)
    to_input = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/input')
    from_input.clear()
    to_input.send_keys(dest)
    time.sleep(0.25)
    pyautogui.press('down')
    time.sleep(0.25)
    pyautogui.press('down')
    time.sleep(0.25)
    pyautogui.press('enter')

    time.sleep(0.25)
    pyautogui.press('enter')

    options = []

    # option 1
    try:                                                                      
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[2]/div/div[4]/div[1]/div/div[2]/div[1]/div/a[1]/div')))
        option_1_element = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[2]/div/div[4]/div[1]/div/div[2]/div[1]/div/a[1]/div')
        option_1_html = option_1_element.get_attribute("innerHTML")
        flight_time_pattern = r'\d+\s?hr\s?\d+\s?min|\d+\s?hr|\d+\s?min'
        price_pattern = r'\$\d{1,3}(?:,\d{3})*'

        flight_time = re.search(flight_time_pattern, option_1_html).group(0)
        price = re.search(price_pattern, option_1_html).group(0)
        options.append((str(price), str(flight_time)))
    except TimeoutException:
        return ("Couldn't load in time", "Couldn't load in time")

    # option 2
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[2]/div/div[4]/div[1]/div/div[2]/div[1]/div/a[2]/div')))
        option_2_element = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[2]/div/div[4]/div[1]/div/div[2]/div[1]/div/a[2]/div')
        option_2_html = option_2_element.get_attribute("innerHTML")
        flight_time_pattern = r'\d+\s?hr\s?\d+\s?min|\d+\s?hr|\d+\s?min'
        price_pattern = r'\$\d{1,3}(?:,\d{3})*'

        flight_time = re.search(flight_time_pattern, option_2_html).group(0)
        price = re.search(price_pattern, option_2_html).group(0)
        options.append((str(price), str(flight_time)))
    except TimeoutException:
        pass

    # option 3
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[2]/div/div[4]/div[1]/div/div[2]/div[1]/div/a[3]/div')))
        option_3_element = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[2]/div/div[4]/div[1]/div/div[2]/div[1]/div/a[3]/div')
        option_3_html = option_3_element.get_attribute("innerHTML")
        flight_time_pattern = r'\d+\s?hr\s?\d+\s?min|\d+\s?hr|\d+\s?min'
        price_pattern = r'\$\d{1,3}(?:,\d{3})*'

        flight_time = re.search(flight_time_pattern, option_3_html).group(0)
        price = re.search(price_pattern, option_3_html).group(0)
        options.append((str(price), str(flight_time)))
    except TimeoutException:
        pass

    times = []
    prices = []
    best_option_price = ()
    best_option_time = ()
    for option in options:
        times.append(option[1])
        prices.append(option[0])
    best_time = shortest_time(times)
    best_price = cheapest_price(prices)
    for option in options:
        if(option[1] == best_time):
            best_option_time = option
        if(int(option[0].replace('$', '').replace(',', '')) == best_price):
            best_option_price = option
    return (str(best_option_price[0]) + ', ' + str(best_option_price[1]), str(best_option_time[0]) + ', ' + str(best_option_time[1]))


city_pairs = []

with open('expanded_cities_list.txt', 'r') as city_file:
    for line in city_file:
        city_pairs.append((('Chicago', line.split(',')[1].strip('\n') + ', ' + line.split(',')[0])))
        city_pairs.append((('Seoul', line.split(',')[1].strip('\n') + ', ' + line.split(',')[0])))

with open('best_price_options.txt', 'w') as price_file:
    with open('best_time_options.txt', 'w') as time_file:
        for pair in city_pairs:
            flight_data = get_flight_data(pair[0], pair[1])
            price_file.write(pair[0] + ',' + pair[1] + ', ' + flight_data[0] + '\n')
            time_file.write(pair[0] + ',' + pair[1] + ', ' + flight_data[1] + '\n')

driver.close()
driver.quit()