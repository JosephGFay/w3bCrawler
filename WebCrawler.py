import requests
from bs4 import BeautifulSoup
import re

# Establish Connection to URL
URL = "https://icl.cyberbit.com/"
page = requests.get(URL)
# Store URL Content into soup object.
html = BeautifulSoup(page.content, "html.parser")

# TODO Write a program that can retrieve and display a site map of any website.

# TODO Retrieve URL from user input


def input_url() -> str:
    return input("[+] Enter a URL: ")


def get_sitemap(url):
    sitemap = requests.get("https://" + url + "/robots.txt")
    return sitemap


if __name__ == '__main__':
    print(get_sitemap(input_url()))
    # prize_list = html.find_all(class_="prizes-content")
    # for prize in prize_list:
    #     title = prize.find("h6").text.strip()
    #     description = prize.find('p').text.strip()
    #     print(f"{title} : {description}")
    #     ipad = re.search('iPad', description)












