"""Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar
to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, 
and parse the data, extracting numbers and compute the sum of the numbers in the file.
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is 
the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1272982.html (Sum ends with 22)
You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
"""

import ssl
import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

sum = 0
count = 0

# ignore SSL Certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    #    print(tag.get('href', None))
    #    print('TAGS: ', tag)
    #    print('URL:', tag.get('href', None))
    #    print('Contents:', tag.contents[0])
    #    print('Attrs:', tag.attrs)
    sum = sum + int(tag.contents[0])
    count = count+1
print('count', count)
print('sum', sum)
