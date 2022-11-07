import re
import time
from pprint import pprint as pr
import requests
from bs4 import BeautifulSoup as BS

def get_ads(page):
    
    def has_data_listing_id(tag):
        return tag.has_attr('data-listing-id')

    def give_correct_type(price_str):
            
        price_str = price_str.replace(',','')
        if price_str[2].isdigit():

            return float(price_str[1:]),price_str[0]
        else:
            return None, None

    def get_date(soap):
        date_str = soap.find(class_='date-posted').text.strip()

        if 'ago' in date_str:

            time_ago, measure_of_time = date_str.split()[1:3]
            if 'minut'in measure_of_time:
                measure_in_sec = 60
            elif 'hour' in measure_of_time:
                measure_in_sec = 60*60
            else:
                measure_in_sec = 1
            time_posted = time.localtime(time.time() - int(time_ago)*measure_in_sec)
            date_posted = f'{time_posted.tm_mday}-{time_posted.tm_mon}-{time_posted.tm_year}'

            return date_posted
        
        else:
            return date_str.replace('/','-')
            
        
    soup = BS(page,'lxml')
    ads = soup.find_all(has_data_listing_id)

    all_ads_from_page = []
    for ad in ads:
        img_url = ad.find('img').get('data-src')

        price_str = ad.find(class_='price').text.strip()
        price, currency = give_correct_type(price_str)
        date = get_date(ad)
        
        all_ads_from_page.append(
            {
                'img-url': img_url,
                'date': date,
                'price': price,
                'currency': currency
            }
        )

    return all_ads_from_page


def save_to_db(ads):
    pass


def main():
    PAGINATION_COUNT = 98 
    
    for i in range(1,PAGINATION_COUNT+1,1):
        
        src = requests.get(url=f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273').text
        ads_from_page = get_ads(src)
        
        pr(ads_from_page)


if __name__ == '__main__':
    main()