def last_even(listn):
    lstn = []
    for i in listn:
        if listn.index(i) % 2 == 0:
            lstn.append(i)
        else:
            pass
    return lstn[-1]
print(last_even([1,2,3,2,42,42,432,4,25,6,7,8,9,56]))