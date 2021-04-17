import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

try:
    response = requests.get(url)

    if response.status_code == 200:
        print(f'Successs, Response = {response.status_code}')
        # print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, "html.parser")
        print(f'Hasil pemanggilan url {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'Ooops ada kesalahan request, status code = {response.status_code}')
except Exception as ex:
    print(f'There is an Error{ex}')

print('Program Ended')