import requests
from bs4 import BeautifulSoup
import re

# Remove this eventually replace with try/catch
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def input_url() -> str:
    # TODO: Add input validation for URL input
    """
    Takes user input in the form of a website URL.

    :return: str
    """
    return input("[+] Enter a URL: ")


def get_robots(url: str) -> requests.Response:
    # TODO: Add validation to check for robots.txt
    """
    Function used to gain access to site map indexes.

    :param url:
    :return: URL with concatenated robots.txt route.
    """
    robots = requests.get("https://" + url + "/robots.txt")
    return robots


def print_sitemap(index: str):

    """
    Output found sitemap XML files to the terminal.

    :param index:
    """
    url = requests.get(index)
    soup = BeautifulSoup(url.content, "html.parser")
    pattern = re.compile('h.+[xml]')

    match_list = re.findall(pattern, soup.text)
    print("[LOG] Displaying route pages:")
    [print(match) for match in match_list]


def get_index() -> str:
    """
    Function used to access a sites map index.

    :return: sitemap_index
    """
    html = BeautifulSoup(get_robots(input_url()).content, "html.parser")
    p = re.compile('h.+[xml]$')
    target = re.search(p, html.text)
    print("[LOG] Sitemap index found: ")
    print(target.group())
    return target.group()


def webmap():
    # TODO: Add validation for top-level function.
    """
    Begins the webmap utility
    """
    print_sitemap(get_index())


if __name__ == '__main__':
    webmap()
