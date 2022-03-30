from bs4 import BeautifulSoup
import requests

url = "https://trickbd.com/"

response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

for image in soup.find_all('img'):
    print(image.get('src'))

product = soup.find_all('div')

