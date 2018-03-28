"""FIXME: Generalize into functions and classes and add argparse blah, blah, blah
"""
import re
from urllib import request
from bs4 import BeautifulSoup


def download_data(url=None, dest=None, verbose=True):
    """Download data from a given URL to a destination.
    """

    if verbose:
        print("Opening request @:", url)

    try:
        req = request.urlopen(url)
    except Exception as err:
        print(err)

    if verbose:
        print("Reading and decoding...")

    try:
        rdata = req.read().decode()

    except Exception as err:
        print(err)

    if verbose:
        print("Writing data to:", dest)

    try:
        with open(dest, "w") as f:
            f.write(rdata)

    except Exception as err:
        print(err)

    if verbose:
        print("Download complete.")


# Grab gitignore files from github's repo
if __name__ == "__main__":

    url = "https://github.com/github/gitignore"


    req = request.urlopen(url)

    html = req.read().decode()

    soup = BeautifulSoup(html, "lxml")


    link_list = []
    for a in soup.find_all('a', href=True):

        if "/blob/master/" in a['href']:

            link_list += [a['href']]

    link_list = list(map(lambda x: "/".join(x.split("/")[4:]), link_list))

    usr = re.sub("https://github.com/", "", url)

    content_url = "https://raw.githubusercontent.com/{}"

    usr_content_url = content_url.format(usr)

    content_links = []
    for i in link_list:
        link = "/".join([usr_content_url, i])
        content_links += [link]


    term = "Python"

    result = list(filter(lambda x: term in x, content_links))

    if len(result) == 1:
        target_url = result[0]
    else:
        target_url = ""
        print(term, ", not found.")

    dest = target_url.split("/")[-1]

    gitignore_dest = "."+dest.split(".")[-1]

    dest = gitignore_dest

    download_data(url=target_url, dest=dest)
