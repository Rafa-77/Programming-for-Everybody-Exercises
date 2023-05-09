#  In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your
# testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_876342.html (Sum ends with 73)

# You need to adjust this code to look for span tags and pull out the text content of the span tag,
# convert them to integers and add them up to complete the assignment.

from urllib.request import urlopen
from bs4 import BeautifulSoup


# url = "http://py4e-data.dr-chuck.net/comments_876342.html"
url = input("Enter - ")
html = urlopen(url).read()
x = BeautifulSoup(html, "html.parser")

tags = x("span")
print(sum([int(tag.contents[0]) for tag in tags]))
