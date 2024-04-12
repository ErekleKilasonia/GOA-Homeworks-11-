#Find Multiples of a Number
def find_multiples(integer, limit):
    listn = []
    for i in range(integer,limit+1,integer):
        listn.append(i)
    return listn