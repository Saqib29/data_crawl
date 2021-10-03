import time
import csv

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from js_func import *


def crawl_data():

    url = "https://www.dsebd.org/latest_share_price_scroll_l.php"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    while True:
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            break
        except Exception as e:
            print(f'chrome downloading problem {e}');

    try: 
       driver.get(url)
       time.sleep(10)
    except:
        print('website hitting problem');

    try:
        data = driver.execute_script(data_collect_func);
    except Exception as e: 
        print(f"problem while data collecting {e}")
    time.sleep(5)

    # print(data);

    driver.close();

    fields = ['TRADING CODE', 'LTP*', 'HIGH', 'LOW', 'CLOSEP*', 'YCP*', 'CHANGE', 'TRADE', 'VALUE (mn)', 'VOLUME', ]
    with open('data.csv', 'w') as f:
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(data)
    
    print('CSV file saving done');


if __name__ == '__main__':
    crawl_data()


                




