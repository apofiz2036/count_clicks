import requests
import os
import argparse

from dotenv import load_dotenv
load_dotenv()


FOR_SHORT_URL = 'https://api-ssl.bitly.com/v4/shorten/'
IS_BITLINK_URL = 'https://api-ssl.bitly.com/v4/bitlinks/'


def main():
    bitly_token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(
        description='Выдаёт битлинк или считает количество переходов'
    )
    parser.add_argument('url', type=str, help='url для запроса')
    args = parser.parse_args()
    url = args.url
    
    if is_bitlink(bitly_token, url):
        print(count_clicks(bitly_token, url))
    else:
        try:
            print(shorten_link(bitly_token, url))
        except requests.exceptions.HTTPError:
            print('Неправильная ссылка')


def is_bitlink(bitly_token, url):
    headers = {'Authorization': f'Bearer {bitly_token}'}
    response = requests.get(f'{IS_BITLINK_URL}{url}', headers=headers)
    return response.ok


def shorten_link(bitly_token, long_url):
    headers = {'Authorization': f'Bearer {bitly_token}'}
    payload = {'long_url': long_url}
    response = requests.post(FOR_SHORT_URL, headers=headers, json=payload)
    response.raise_for_status()
    bit_link = response.json()['id']
    return bit_link


def count_clicks(bitly_token, url):
    headers = {'Authorization': f'Bearer {bitly_token}'}
    response = requests.get(f'{IS_BITLINK_URL}{url}/clicks/summary')
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


if __name__ == '__main__':
    main()