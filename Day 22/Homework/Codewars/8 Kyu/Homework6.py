#Vowel remover
def shortcut( s ):
    str = "aeiou"
    listn = []
    
    for i in s:
        listn.append(i)
        for x in str:
            if i == x:
                listn.remove(i)
    return "".join(listn)
        