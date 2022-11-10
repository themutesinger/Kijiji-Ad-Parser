import time

from bs4 import BeautifulSoup as BS


def has_data_listing_id(tag):
    return tag.has_attr('data-listing-id')

def give_correct_type(price_str):
        
    price_str = price_str.replace(',','')
    if price_str[2].isdigit():

        return float(price_str[1:]),price_str[0]
    else:
        return None, None

def get_date(soup):
    date_str = soup.find(class_='date-posted').text.strip()

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
        

def get_ads(page):
    
        
    soup = BS(page,'lxml')
    ads = soup.find_all(has_data_listing_id)
    pagination = int(soup.find(class_='selected').text)

    all_ads_from_page = []
    for ad in ads:
        img_url = ad.find('img').get('data-src')
        title = ad.find(class_='title').text.strip()
        price_str = ad.find(class_='price').text.strip()
        price, currency = give_correct_type(price_str)
        date = get_date(ad)
        
        
        all_ads_from_page.append(
            {   
                'title': title,
                'img-url': img_url,
                'date': date,
                'price': price,
                'currency': currency,
                'pagination': pagination
            }
        )

    return all_ads_from_page

