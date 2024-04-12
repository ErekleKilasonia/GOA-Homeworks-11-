def even_numbers(listn):
    counter = 0
    for i in listn:
        if i % 2 == 0:
            counter += 1
        else:
            pass
    return counter
print(even_numbers([1,2,3,4,5,6,7,8,9,0]))