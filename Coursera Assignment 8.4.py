"""8.4) Open the file 'romeo.txt' and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append
 it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt """

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word = line.split()
    for lines in word:
        nword = lines.split()
        for i in nword:
            if nword not in lst:
                lst.append(i)

print(sorted(set(lst)))


# different method
"""fname = input("Enter file name: ")
fh = open(fname)
lst = list()
nlst = list()
for line in fh:
    word = line.split()
    for lines in word:
        nword = lines.split()
        for i in nword:
            lst.append(i)
        for i in lst:
            if i not in nlst:
                nlst.append(i)

print(sorted(nlst))
"""
