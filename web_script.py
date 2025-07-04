import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://news.ycombinator.com/'

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find and print all article titles (example: all <a> tags with class 'titlelink')
for title in soup.find_all('a', class_='titlelink'):
    print(title.text)
