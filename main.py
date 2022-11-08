from pprint import pprint as pr

import requests

from ad_parser import get_ads
import save_dict_to_db



def main():
    pagination_count = int(input('How many pages do you want? >>> '))
    
    for i in range(1,pagination_count+1,1):
        
        src = requests.get(url=f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273').text
        ads_from_page = get_ads(src)
        
        pr(ads_from_page)


if __name__ == '__main__':
    main()