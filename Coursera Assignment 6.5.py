text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(':')
print(pos)
npos = text.find('5')
print(npos)
data = text[pos+1: npos+1].lstrip()
print(float(data))
