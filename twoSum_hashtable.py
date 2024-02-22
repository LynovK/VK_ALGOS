def twoSum (data,target):
    cache = dict()
    # map[int]int
    for i in range(0, len(data)):
        if contains