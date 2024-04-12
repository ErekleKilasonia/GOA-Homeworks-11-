#Calculate average
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        x  = sum(numbers) / len(numbers)
        y = round(x, 3)
        return y 