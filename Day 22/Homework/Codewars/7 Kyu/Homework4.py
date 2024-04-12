#Printer Errors
def printer_error(s):
    counter = 0
    num = 0
    str1 = "abcdefghijklm"
    for x in s:
        if x in str1:
            counter+=1
        else:
            counter+=1
            num+=1
            
    return str(num) + "/" + str(counter)
        