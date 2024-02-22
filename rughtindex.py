def rightindex():
    i = input()
    arr = [i for i in input().split()]
    target = input()
    r = len(arr) - 1
    left = 0
    while left <= r:
        mid = (left+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            r = mid -1
    return left
print(rightindex())