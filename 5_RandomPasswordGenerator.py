import random

def randomPassWord():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to Password Generator!")
 
    choice=False
    while not choice:
      nr_letters = int(input(f"How many letters would you like in your password?\n"))
      nr_symbols = int(input(f"How many symbols would you like?\n"))
      nr_numbers = int(input(f"How many numbers would you like?\n"))
      if nr_letters in range(0,100) and nr_symbols in range(0,100) and nr_numbers in range(0,100):
        choice=True

      else:
        print("Either out of range or incorrect input:\n")
        choice=False

    
    password_list = []
    for char in range(1, nr_letters + 1):
      password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
      password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)
      
      random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
randomPassWord()
