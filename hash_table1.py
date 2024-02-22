tmp = int(input())
a = str(input()).split(", ")
q = []
for i in a:
    q.append(int(i))
hash = dict()
for i in q:
    if i in hash:
        hash[i] +=1
    else: hash[i] = 1
m = max(hash.values())
r = tmp/2
dict_i = hash.items()
if m > r:
    for key,value in dict_i:
        if value == m:
            print(int(key))


else: print(-1)
