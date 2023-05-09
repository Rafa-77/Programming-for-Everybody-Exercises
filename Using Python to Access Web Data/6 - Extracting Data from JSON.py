# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse
# and extract the comment counts from the JSON data, compute the sum of the numbers in the file and
# enter the sum below:
# Actual data: http://py4e-data.dr-chuck.net/comments_876345.json (Sum ends with 48)
import ssl
from urllib.request import urlopen
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_876345.json"
html = urlopen(url)
data = html.read()
info = json.loads(data)
# print(data.decode())
count = 0

print("Retrieved", len(data), "characters")
for item in info["comments"]:
    count += 1

print("Count:", count)
print("Sum:", sum([int(item["count"]) for item in info["comments"]]))
