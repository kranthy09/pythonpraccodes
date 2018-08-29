a = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
s = sorted(set([x[1] for x in a]))
print(s)
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print(name)
print(a[1])