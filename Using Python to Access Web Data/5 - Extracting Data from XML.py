# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.

# Actual data: http://py4e-data.dr-chuck.net/comments_876344.xml (Sum ends with 94)

import urllib.request
import xml.etree.ElementTree as ET


url = "http://py4e-data.dr-chuck.net/comments_876344.xml"
html = urllib.request.urlopen(url).read()
print("Retrieved", len(html), "characters.")

tree = ET.fromstring(html)
result = tree.findall(".//count")
print("Count:", len(result))

print("Sum:", sum([int(element.text) for element in result]))
