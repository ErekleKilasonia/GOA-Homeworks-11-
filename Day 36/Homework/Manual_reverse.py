def manual_reverse(list):
    listn = []
    for i in list:
        listn.insert(0,i)
    return listn
print(manual_reverse([1,2,3,4,5,6]))