dictionary = {}
length = int(input())
for i in input().split():
    dictionary[i] = i
target = input()
if target in dictionary:
    print(True)
else: print(False)