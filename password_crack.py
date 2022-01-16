# Python3
import random
character ="0123456789"
char_list = list(character)
print("")
print("Please type numbers <=6 ")
password= input("Enter Your password: ")
guess_password=''

while (guess_password != password):
    guess_password= random.choices(char_list, k=len(password))
    print(str(guess_password) + "            Failed!")
    
    if(guess_password == list(password)):
        print("  Password Found!     "+"".join(guess_password))
        
        break
