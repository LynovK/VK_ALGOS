def feedAnimals (animals, food):
    animals = [i for i in input().split()]
    food = [i for i in input().split()]
    if len(animals) == 0 or len(food) == 0:
        return 0
    count = 0
    an = animals.sort()
    foo = food.sort()
    for f in foo:
        if len(an) > count:
            if f >= an[count]:
                count += 1
            if count == len(animals):
                break
    return count
