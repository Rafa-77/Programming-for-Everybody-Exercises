# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Carmen.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: D

from urllib.request import urlopen
from bs4 import BeautifulSoup

position = 18
number_of_counts = 7
to_get = 0
url = "http://py4e-data.dr-chuck.net/known_by_Carmen.html"


while to_get < number_of_counts:
    html = urlopen(url).read()
    x = BeautifulSoup(html, "html.parser")

    links = x("a")
    names = ([link.contents[0] for link in links])
    go = ([link.get("href", None) for link in links])
    print("Name #", to_get + 1, ": ", names[position-1], sep="")
    to_get += 1
    url = go[position-1]
