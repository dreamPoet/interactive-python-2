l = [0, 1]
for i in range(40):
    l.append(l[i] + l[i+1])

print l[-1]