import random

def startGame():
    Lives=0   
    
    def game():
        print("Welcome To Number Guessing Game")    
    notRight = False
    while not notRight:
        Level=input('Select Level "Easy" Or "Hard" ').lower()
        if Level=="easy":
            Lives+=10
            notRight=True
            
        elif Level=="hard":
            Lives+=5
            notRight=True
            
        else:
            print("Wrong Choice")
    notRight=False
    

    print(f"You have {Lives} Lives.")
    choice=False

    randomNumber = random.randint(1, 101)
    
    while not choice:
        checkGuess=False
        
        Guess=int(input("Guess a Number between 1 and 100:\n"))
        
        
        while not checkGuess:           
            if type(Guess)==int:
                checkGuess=True
            else:
                print("Enter a  Number.")
                checkGuess=False
        
        if Guess==randomNumber:
            print(f"You Win.The number is {randomNumber}.")
            checkGuess=True
            choice=True
        elif Guess>randomNumber:
            print("Too High")
            Lives-=1
            print(f"You Have {Lives} Lives left:")
        elif Guess<randomNumber:
            Lives-=1
            print("Too Low")

            print(f"You Have {Lives} Lives left:")
           
        else:
            print("Wrong Guess a number")

        if Lives==0:
            print(f"You Lose The Number is {randomNumber} ")
            choice= True



startGame()