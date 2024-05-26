def manual_count(list,to_count):
    count = 0
    for i in list:
        if i == to_count:
            count += 1
    return count
print(manual_count([1,2,2,2,3,4,5,7],2))