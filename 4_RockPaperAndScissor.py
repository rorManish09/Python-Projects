rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



import random
images=[rock,paper,scissors]
user_choice=int(input("What do you want to choose?Type 0 for rack or 1 for paper and 2 for scissors"))
computer_choice=random.randint(0,2)

if user_choice>=3 or user_choice<0:
    print("You typed invalid number")
else:    
    print(images[int(user_choice)])
    print("Computer chose:")
    print(images[int(computer_choice)])

   
    if user_choice==0 and computer_choice==2:
        print("You win")
    elif computer_choice==0 and user_choice ==2:
        print("You lose")
    elif  user_choice>computer_choice:
        print("You win")
    elif user_choice<computer_choice:
        print("You lose")
    elif computer_choice==user_choice:
        print("Its a draw!")

