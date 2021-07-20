"""In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the 
process a number of times and report the last name you find.
We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other
is the actual data you need to process for the assignment
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. 
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Susannah.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: A
"""
import ssl
import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup


# ignore SSL Certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
count = int(input('Count: '))
position = int(input('Positon: '))

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    reff = list()
    text = list()
    for tag in tags:
        x = tag.get('href', None)
        reff.append(x)
        y = tag.text
        text.append(y)

    # print(reff[position-1])
    print(text[position-1])
    url = reff[position-1]
