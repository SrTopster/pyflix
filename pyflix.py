#!/bin/python3
import requests
import sys
import os
from bs4 import BeautifulSoup

def soup_maker(url):
    return BeautifulSoup(requests.get(url).content,"lxml")
links = []
for a in soup_maker("https://1337x.wtf/search/{}/1/".format("+".join(sys.argv[1:]))).find_all("a"):
    if  a.get("href").startswith("/torrent/"):
        links.append({"title":a.text,"link":a.get("href")})
        if len(links)>9:
            break
for i in links:
    print("\033[92m[{}]\033[0m".format(links.index(i)+1),i["title"])
for a in soup_maker("https://1337x.wtf"+links[int(input("> "))-1]["link"]).find_all("a"):
    if a.get("href").startswith("magnet:?xt=urn:"):
        os.system("peerflix -k {} &".format(a.get("href")))
        break