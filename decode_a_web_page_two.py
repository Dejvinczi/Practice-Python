"""
Using the requests and BeautifulSoup Python libraries, print to the screen the
full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print
out the text to the screen so that you can read the full article without having
to click any buttons.

This will just print the full text of the article to the screen. It will not
make it easy to read, so next exercise we will learn how to write this text
to a .txt file.
"""
import requests
from requests import HTTPError
from bs4 import BeautifulSoup


url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'

try:
    res = requests.get(url)
except HTTPError as e:
    print(e.response.text)


soup = BeautifulSoup(res.text, features="html.parser")
all_p_cn_text_body = soup.select("body__inner-container > p")
print(all_p_cn_text_body)
for elem in all_p_cn_text_body[7:]:
    print(elem.text)
