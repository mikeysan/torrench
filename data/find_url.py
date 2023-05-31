'''
Copyright (C) 2017 Rijul Gulati <kryptxy@protonmail.com>

This file is part of Torrench.

Torrench is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Torrench is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>. 
'''

from bs4 import BeautifulSoup
import requests

url = "https://thepiratespace.org/"
raw = requests.get(url)
raw = raw.content
soup = BeautifulSoup(raw, "lxml")
links = soup.find_all('td', {'title': 'URL'}, limit=2)
myList = []
def find_url_list():
	global url
	for i in links:
     myList.append(i.a["href"])
	# If myList is empty, append the original URL
	if not myList:
     myList.append(url)
     
    return myList

if __name__ == "__main__":
	print("It's a module. Can only be imported!");
