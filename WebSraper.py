from bs4 import BeautifulSoup
import requests

url = "https://trickbd.com/"

response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

print(soup.title)
"""print(response.content)
soup = BeautifulSoup("")
print(soup.prettify())"""
