def hangman(word):
    x = 6
    listn = []
    lstn = []
    print(f"Word lenght is {len(word)} and remember that you have 6 tries.")
    for z in word.lower():
        listn.append(z.lower())
    while x >= 0:
        if x == 0:
            print("You lost😢")
            break
            
        y = input("Enter a letter or a word: ")
        if y in lstn:
            if len(y) == 1:
                print("Try again you already have guessed that letter and it was wrong")
            elif len(y) > 2:
                print("Try again you already have guessed that letters and it was wrong")
        elif y.lower() == word.lower():
            print("You have guessed the word!")
            x-= 6
        elif y.lower() in word.lower() and len(y) >= 2:
            print(f"Your guess is right and {y[0]} is on position {listn.index(y[0])+1}")
        elif y.lower() in word.lower():
            print(f"Your guess is right and its on position {listn.index(y.lower())+1}")
        else:
            x -= 1
            lstn.append(y)
            if x >1:
                print(f"Your guess is wrong and you have {x} tries left")
            elif x == 1:
                print(f"Your guess is wrong and you have {x} try left")
        
hangman("")

        