"""The basic outline of this problem is to read the file, look for integers using the re.findall(),
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers."""

import re
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
count = 0
sum = 0
for line in fh:
    line = line.rstrip()
    data = re.findall('[0-9]+', line)
    lst = lst + data

for num in lst:
    sum = sum + int(num)
    count = count+1
print(sum)
print(count)
