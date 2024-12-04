word=list(input("enter a word"))
newlist=['_' for x in word]
a=len(word)
for x in range(a+2):
    letter=input("enter a letter")
    if letter in word:
        print("guess is correct")
        for i in range(a):
            if word[i]==letter:
                newlist[i]=letter
                print(newlist)
        if newlist==word:
            print("you won the game")
            break
    else:
        print("guess is not correct")
else:
    print("you failed")