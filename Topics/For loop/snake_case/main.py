word = input()
s = ""
for x in word:
    if x.isupper():
        s = f"{s}_{x.lower()}"
    else:
        s = f"{s}{x}"
print(s)
