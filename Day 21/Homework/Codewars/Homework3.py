#Vowel Count
def get_count(sentence):
    num_vow = 0
    vowels ="aeiou"
    for i in sentence:
        if i in vowels:
            num_vow = num_vow + 1
    return num_vow