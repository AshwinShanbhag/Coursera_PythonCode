"""10.2 Write a program to read through the 'mbox-short.txt' and figure out the distribution by hour of the day for each of the messages.
 You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):

        continue
    wds = line.split()
    # print(wds)
    for wd in wds:
        if not wd == wds[5]:
            continue
        nwd = wd.split(':')  # time split
        for w in nwd:
            if w == nwd[0]:
                di[w] = di.get(w, 0)+1
            break  # to break from the loop so that it doesn't go to second index while incrementing

# to reverse the order and sorting it in order of values
"""tmp = list()
tmp = sorted([(v, k)for k, v in di.items()], reverse=True)
print(sorted(tmp))
"""
for k, v in sorted(di.items()):
    print(k, v)
