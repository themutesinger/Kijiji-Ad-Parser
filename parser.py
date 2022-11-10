import requests
from tqdm import tqdm

from service.ads_getter import get_ads
from service.saving_to_db import save_to_db




def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8'
    }
    pagination_count = int(input('How many pages do you want? >>> '))
    
    for i in tqdm(range(1,pagination_count+1,1)):
        src = requests.get(url=f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273', headers=headers).text
        ads_from_page = get_ads(src)
        save_to_db(ads_from_page)


if __name__ == '__main__':
    main()