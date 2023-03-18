from art import logo

print(logo)
#Here is the Encryption function
def cesar(Starting_text,shift_number,Cipher_direction):
    ending_text=""
    if shift_number>25:
        shift_number%=25

    if Cipher_direction=="decode":
        shift_number*=-1
        for letter in Starting_text:
            position=alphabet.index(letter)
            new_positon=position+shift_number
            ending_text+=alphabet[new_positon]
    print(f"The {Cipher_direction}d text is {ending_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
choice = False
while not choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar(Starting_text=text, shift_number=shift, Cipher_direction=direction)

    Again_Start=input("Do you want to start again Y if not press any key?").lower()
    if Again_Start=="y":
        choice=False
    else:
        choice=True
        print("See You Soon")
    
     