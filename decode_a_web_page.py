"""
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage (https://www.nytimes.com).
"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com'
res = requests.get(url)

if res.status_code != 200:
    raise Exception(res.errors)

soup = BeautifulSoup(res.text, features='html.parser')

for story_heading in soup.find_all(class_="indicate-hover"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
