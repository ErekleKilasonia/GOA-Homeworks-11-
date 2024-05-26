def name_in_str(strng : str, name : str) -> bool:
    strng = strng.lower()
    name = name.lower()
    count1 = 0
    count2 = 0
    while count1 < len(strng) and count2 < len(name):
        if strng[count1] == name[count2]:
            count2 += 1
        count1 += 1
    return True if count2 == len(name) else False