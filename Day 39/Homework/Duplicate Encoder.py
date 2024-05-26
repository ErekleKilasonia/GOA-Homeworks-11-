def duplicate_encode(word):
    word = word.lower()
    string1 = ""
    for i in word:
        if word.count(i) == 1:
            string1 += "("
        elif word.count(i) > 1:
            string1 += ")"
    return string1
            