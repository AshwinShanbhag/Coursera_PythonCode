"""
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL,
read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need
to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1272984.xml (Sum ends with 64)
You do not need to save these files to your folder since your program will read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
"""
import ssl
import urllib.request
import urllib.parse
import urllib.error
import ssl
import xml.etree.ElementTree as ET

lst = list()
sum = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx)
data = html.read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

for items in lst:
    counts = items.find('count').text  # counts = items.find('.//count').text
    sum = sum+int(counts)

print(sum)
