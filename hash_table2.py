s = str(input()).split(", ")
a = s[0]
b = s[1]

hash = dict()
hash2 = dict()

if len(a) != len(b):
    print("false")
else:
    for i in a:
        if i in hash:
                hash[i] += 1
        else: hash[i] = 1
    for i in b:
        if i in hash2:
                hash2[i] += 1
        else: hash2[i] = 1
    if hash == hash2:
        print("true")
    else:
        print("false")

