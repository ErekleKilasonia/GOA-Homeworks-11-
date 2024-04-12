def even_index(listn):
    lstn = []
    for i in listn:
        if listn.index(i) % 2 == 0:
            lstn.append("$")
        else:
            lstn.append(i)
    return lstn
print(even_index([1,2,3,52,4525,4,46,7,3,5,65,89]))