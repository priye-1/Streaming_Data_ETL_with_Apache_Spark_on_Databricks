import requests
from typing import List, Dict
from datetime import datetime


def get_stock_data() -> List[Dict]:
    """Function to scrape data from CNN API

    Returns:
        json: Stock market results

    Sample output:
        [
            {
                'name': 'Nasdaq',
                'symbol': 'COMP-USA',
                'current_price': 12284.74316868,
                'prev_close_price': 12328.5065042,
                'price_change_from_prev_close': -43.76333552000142,
                'percent_change_from_prev_close': -0.003549767808865769,
                'prev_close_date': '2023-05-11',
                'sort_order_index': 0,
                'last_updated': '2023-05-12T21:16:26+00:00',
                'event_timestamp': '2023-05-12T21:16:26+00:00',
                'status': 'UNKNOWN',
                'next_status': 'UNKNOWN',
                'next_status_change': '2023-05-12T13:30:21.109002+00:00',
                'country': {'name': 'United States', 'code': 'USA', 'region': 'Americas'},
                'refresh_interval_in_seconds': 0
            }
        ]
    """

    today_date = datetime.now().strftime("%Y-%m-%d")

    url = f"https://production.dataviz.cnn.io/markets/world/regions/Americas,Asia-Pacific,Europe/{today_date}"

    payload = {}
    headers = {
        'authority': 'production.dataviz.cnn.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,my-ZG;q=0.8,my;q=0.7',
        'cache-control': 'no-cache',
        'origin': 'https://edition.cnn.com',
        'pragma': 'no-cache',
        'referer': 'https://edition.cnn.com/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()