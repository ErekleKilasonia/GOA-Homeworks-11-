#Descending Order
def descending_order(num):
    x = sorted(str(num), reverse=True)
    y = "".join(x)
    return int(y)  
