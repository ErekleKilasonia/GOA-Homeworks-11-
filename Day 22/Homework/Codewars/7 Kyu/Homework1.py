#Reverse words
def reverse_words(text):
    listn = text.split()
    lstn = []
    for i in listn:
        lstn.append(i[::-1])
    x = ' '.join(lstn)
    y = '  '.join(lstn)
    if len(text) == len(x):
        return x
    else:
        return y