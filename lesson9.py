'''
import urllib.request

opener = urllib.request.build_opener()
response = opener.open('http://www.google.com')
print(response.read())
'''
'''
import requests

response = requests.get('http://httpbin.org')
print(response.text)
print(response.content)
print(f"Datatype: {type(response.content)}")
'''
from bs4 import BeautifulSoup
import requests
url = "http://www.google.com"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    soup_list = soup.find_all("a", {"herf": "/currencies/bitcoin/#markets"})
    for item in soup_list:
        print("elem")
