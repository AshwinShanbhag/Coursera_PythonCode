import urllib.request
import urllib.parse
import urllib.error
counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().strip()
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)
