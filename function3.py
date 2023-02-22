def garyvee(s):
    if s > 0:
        return s
    else:
        return -s

for i in range(-100,101):
    print(f"|{i}| = {garyvee(i)}")
