from bs4 import BeautifulSoup as bs
import requests

r = requests.get('https://tabs.ultimate-guitar.com/tab/pink-floyd/shine-on-you-crazy-diamond-part-i-v-tabs-513655')

print(bs(r.text))