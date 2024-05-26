def manual_replace(list,to_replace):
    for i in range(len(list)):
        if list[i] == to_replace[0]:
            list[i] = to_replace[1]
    return list
print(manual_replace([1,2,3,4,5,6,6,7,8],[6,9]))