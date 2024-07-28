import random
random_num=random.randint(1000,9999)

#to identify the random number generated
print(random_num)

print("Enter zero to quit the game")
user_num=int(input("Enter a four digit number:"))
while user_num!=0:
    num=random_num

    #to count the number of digits guessed correct
    correct_count=0
    
    while num%10:
        game_num=num%10
        guess_num=user_num%10
        num=num//10
        user_num=user_num//10
        if game_num==guess_num:
            correct_count=correct_count+1
            
    if correct_count==4:
        print("congrats! you guessed it right")
        break
    else:
        print(correct_count,"digits were guessed correct")
        user_num=int(input("Enter a four digit number:"))
else:
    print("You quit the game")