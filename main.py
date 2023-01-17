import os
import re
import time
import codecs
import quopri
import pathlib 
import pyautogui
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

script_directory = pathlib.Path().absolute()
# DRIVER_PATH = f'{script_directory}\chromedriver_win32\chromedriver.exe' 

# chrome_options = Options()
# chrome_options.add_argument(f'user-data-dir={script_directory}\selenium') 
# chrome_options.add_argument('--save-page-as-mhtml') 
# # chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
# driver.get('https://shopee.com.my/cart')  
# select_all_checkbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'container')))
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.find_elements(By.CSS_SELECTOR, '.stardust-checkbox')[-1].click()    

# while len(driver.find_elements(By.XPATH, "//div[contains(.,'All Rights Reserved')]")) == 0:
#     print("in loop")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

# current_time = datetime.now().strftime('%Y_%m_%d_%H_%M')
# filepath = f'{script_directory}\html\shopee_cart_{current_time}.mhtml'

# # res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
# # with open(filepath, 'w', newline='', encoding='utf-8') as f:   
# #     f.write(res['data'])

# # with open(filepath, 'w', encoding='utf-8') as f:
# #     f.write(driver.page_source)

# time.sleep(5)
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# pyautogui.typewrite(filepath) 
# # time.sleep(3)
# # pyautogui.hotkey('tab') 
# # time.sleep(3)
# # pyautogui.hotkey('down')  
# # time.sleep(3)
# # pyautogui.hotkey('up')  
# # time.sleep(3)
# # pyautogui.hotkey('enter') 
# time.sleep(3)
# pyautogui.hotkey('enter') 

# time_to_wait = 100
# time_counter = 0
# while not os.path.exists(filepath) and time_counter<=time_to_wait:
#     time.sleep(1)
#     time_counter += 1 

html_path = f'{script_directory}\html\shopee_cart_2023_01_17_21_26.mhtml'
with open(html_path, encoding='utf-8') as f:
    raw_html = f.read()
 
with open('html/test.mhtml', 'w') as f:
    f.write(raw_html) 
    
soup = BeautifulSoup(quopri.decodestring(raw_html) , 'html.parser')

shop_items_div = "QetDXz"
shop_url_a = "aDk6VO"
shop_name = [i.find('span').text for i in soup.find_all('a', class_=shop_url_a)]
item_img_div = "_9OEiWk"
price_div = "_3+V9JZ"
item_name_a = "kjRybG"
item_url = [i['href'] for i in soup.find_all('a', class_=item_name_a)]
item_img_url_div = "bkwjpc"
item_img_url = [re.search(r'\("(.*?)"\)', i['style'])[0][2:-2] for i in soup.find_all('div', class_=item_img_url_div)]

print(item_url)
print(shop_name)
print(item_img_url)


# container = soup.find_all('div', class_='container')[1]
# inner_container = container.find("div", {"role":"main"})
# items = inner_container.findChildren('div', recursive=False)[2:]  
# items = [item.findChildren('div', recursive=False)[1] for item in items]
# items = [item.findChildren('div', recursive=False)[0] for item in items]
# items = [item.findChildren('div', recursive=False)[0] for item in items]


# first_price = container.find("span", string=re.compile(r'^RM[0-9]+.[0-9]{2}$')) 
# first_price_class = first_price.attrs['class'][0]
# span_class = soup.select(f'span[class={first_price_class}]')[0]
# first_shop_class = span_class.parent.parent.parent.parent.attrs['class'][0]
# div_per_shop = container.find_all('div', class_=first_shop_class) 
 
# for shop in div_per_shop:
#     for items in shop: 
#         items_attr = items.find_all('div', recursive=False)
#         img_title = items_attr[1].find('div', recursive=False)
#         # img_title = img_title.select_one('div>div')

#         url = img_title.select_one('a>div')['style']
#         url = re.search(r'\("(.*?)"\)', url)[0][2:-2]
#         href = img_title.find('a')['href']
#         title = img_title.find('a')['title']
#         price = items_attr[3].select(f'span[class={first_price_class}]')[0].getText() 
#         print(url)
#         print(href)
#         print(title)  
#         print(price)
#         print("\n")

