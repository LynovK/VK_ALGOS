# def extraLetter(a,b):
#     a = str(input())
#     b = str(input())
#     hashMapB = dict{}
#     for i in range(0, len(b)):
#         hashMapB[b[i]] +=1
#     for i in range(0, len(a)):
#         if contains(hashMapB, a[i]):
#             hashMapB[a[i]] -= 1
#     for letter, count = range(hashMapB):
#         if count > 0:
#             return letter
#     return ""
#