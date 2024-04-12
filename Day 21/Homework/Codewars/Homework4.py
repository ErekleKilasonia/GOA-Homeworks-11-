#Square Every Digit
def square_digits(num):
    x = ""
    for i in str(num):
        x = x + str(int(i)**2)
        
    return int(x)
        
        