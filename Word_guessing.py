import random
name=input("What is your name?:")
print("Good luck!",name)
words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board']
word=random.choice(words)
print("Guess the characters in the word")
guesses=''
turns=20
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=' ')
        else:
            print('_')
            failed+=1
    if failed==0:
        print("\nYou Won")
        print("\nThe word is:",word)
        break
    print()
    guess=input("\nGuess a character in the word:")
    guesses+=guess
    if guess not in word:
        turns-=1
        print('\nWrong')
        print('\nYou have {} turns to guess the characters'.format(turns))
        if turns==0:
            print("\nYou lost")