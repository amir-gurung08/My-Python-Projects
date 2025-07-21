
import random
'''
1 for snake
-1 for water
0 for gun


'''

computer = random.choice([0,1,-1])

user = input("Enter Your Choice: ")

user_dict = {"s" : 1, "w" : -1, "g" : 0}
computer_dict = {1 : "Snake",-1 : "Water",0 : "Gun"}

userin = user_dict[user]

print(f"Computer Choose : {computer_dict[computer]} and You Choose: {computer_dict[userin]}")

if computer == userin:
    print("It's a Draw")
else:
    if(computer == 1 and userin == -1):
        print("You Loose")

    elif(computer == -1 and userin == 0):
        print("You Loose")

    elif(computer == 0 and userin == 1):
        print("You Loose")

    elif(computer == -1 and userin == 1):
        print("You Win")

    elif(computer == 0 and userin == -1):
        print("You Win")

    elif(computer == 1 and userin == 0):
        print("You Win")

    else:
        inprint("Something Went Wrong")