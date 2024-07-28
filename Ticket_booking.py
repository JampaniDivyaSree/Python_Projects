class Tickets_booking:
    def Movie(self,list,n):
        self.name=list[0]
        self.hero=list[1]
        self.heroine=list[2]
        self.total_seats=int(list[3])
        self.blocked=int(list[4])
        self.reserved=int(list[5])
        self.remaining=self.total_seats-(self.blocked+self.reserved+n)
        if self.remaining<=0:
            print("seats are full")
            exit()
        print("Ticket details")
        print("--------------------------------------------")
        print("Movie info","\nTittle:",self.name,"\nHero:",self.hero,"\nHeroine:",self.heroine,"\ntotal_seats:",self.total_seats,"\nremaining_seats:",self.remaining)
        print("--------------------------------------------")
        return "successful"
        #return self.remaining
    
choice1=["thriller1","hero_1","heroine_1",100,20,50]
choice2=["thriller2","hero_2","heroine_2",200,30,20]
choice3=["thriller3","hero_3","heroine_3",300,20,50]
choice4=["thriller4","hero_4","heroine_4",400,40,10]
choice5=["thriller5","hero_5","heroine_5",500,60,30]

print("Movie details")
print(choice1,"\n",choice2,"\n",choice3)
user_input=int(input("Enter your movie_choice(1-5):"))
n=int(input("Enter number of tickets for booking:"))
if user_input == 1:
    selected_choice = choice1
elif user_input == 2:
    selected_choice = choice2
elif user_input == 3:
    selected_choice = choice3
elif user_input == 4:
    selected_choice = choice4
elif user_input == 5:
    selected_choice = choice5
else:
    print("Invalid movie choice.")
    exit()
t=Tickets_booking()
booking=t.Movie(selected_choice,n)
print("Booking is:",booking)