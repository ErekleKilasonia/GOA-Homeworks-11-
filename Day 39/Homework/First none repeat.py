def first_non_repeating_letter(s):
    strng = ""
    for i in s:
        if s.lower().count(i.lower()) == 1:
            strng += i
    if strng == "":
        return strng
    else:
        return strng[0]