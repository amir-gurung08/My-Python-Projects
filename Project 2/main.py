from random import randint as ran

class game:
    def __init__(self):
        self.a = ran(1, 50)
        self.guess = 0


    def check(self):
        while True:
            user = int(input("Guess The Number (1-50): "))
            self.guess += 1

            if user > self.a:
                print("Try! Lower Number Please")
            elif user < self.a:
                print("Try! Higher Number Please")
            elif user == self.a:
                print("Congratuation! Your Guessed Number is Correct")
                break
            else:
                print("The Guess is not correct! Try Again")

        print(f"You have Guessed Correct Number {self.a} in {self.guess} tries")


high = game()

while True:
    passw = input("Enter the password to open the game: ")
    if passw == "amir":
        high.check()
        break
    else:
        print("Wrong password! Try Again")
