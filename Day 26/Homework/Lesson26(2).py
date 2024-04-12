def max_number(numbers):
    i = numbers[0]
    for x in numbers:
        if x > i:
            i = x
    return i
print(max_number([1,2312,543,5643,24234,6,3]))