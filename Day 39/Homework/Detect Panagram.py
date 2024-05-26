def is_pangram(s):
    y = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    count = 0
    x = set()
    for z in s.lower():
        if z in y:
            x.add(z)
        else:
            pass
    for i in x:
        count += 1
    if count == 26:
        return True
    else:
        return False
    