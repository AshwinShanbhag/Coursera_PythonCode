"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates
 a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the
 dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
 """

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mail = dict()


for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    wds = line.split()
    for nw in wds:
        if nw == wds[1]:
            mail[nw] = mail.get(nw, 0)+1
maxv = 0
maxw = None
for k, v in mail.items():
    if v > maxv:
        maxv = v
        maxw = k

print(maxw, maxv)
