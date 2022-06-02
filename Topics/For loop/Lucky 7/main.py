import string
lc = string.ascii_lowercase
d = {}
for c in lc:
    d[c] = c+c
print(d)