def permutations(s):
    import random
    sets = set()
    listn = []
    for i in s:
        listn.append(i)
    for i in range(250000):
        random.shuffle(listn)
        sets.add("".join(listn))
    return sets