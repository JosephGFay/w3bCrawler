import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# html = BeautifulSoup(page.content, "html.parser")

# TODO Write a program that can retrieve and display a site map of any website.

# TODO Retrieve URL from user input


def input_url() -> str:
    return input("[+] Enter a URL: ")


def get_robots(url: str) -> requests.Response:
    robots = requests.get("https://" + url + "/robots.txt")
    return robots


def get_sitemap(index: str):
    url = requests.get(index)
    soup = BeautifulSoup(url.content, "html.parser")
    p = re.compile(('[h].+[xml]'))

    match_list = re.findall(p, soup.text)
    print("[LOG] Displaying route pages:")
    [print(match) for match in match_list]


if __name__ == '__main__':
    html = BeautifulSoup(get_robots(input_url()).content, "html.parser")
    p = re.compile('[h].+[xml]$')
    target = re.search(p, html.text)
    print("[LOG] Sitemap index found: ")
    print(target.group())

    get_sitemap(target.group())
    # prize_list = html.find_all(class_="prizes-content")
    # for prize in prize_list:
    #     title = prize.find("h6").text.strip()
    #     description = prize.find('p').text.strip()
    #     print(f"{title} : {description}")
    #     ipad = re.search('iPad', description)












