#Copyright 2021 Joegakumo
#author:Joseph Gakumo
#standard lib exxports
import random
max_number=20

max_geuses=5
number_of_geuses=0

number_to_geuse = random.randint(1,max_number)


print("Hi user, welcome to guese number game")

is_valid=False

while number_of_geuses < max_geuses:
    
    while not is_valid:
        print("Please enter a number between 1 and 20")
        
        try:
            user_number=int(input("Enter your gues number\n"))
        except:
            print("The value you entered was not a number")
            continue

        if user_number >0 and user_number<=max_number:
            is_valid = True 



    if user_number == number_to_geuse:
        print(f"Congratulation  you are perfect in making the geuse ,the correct number guese was {number_to_geuse}")
        break 
    elif number_of_geuses < (max_geuses-1):
        number_of_geuses+=1
        is_valid=False
        print("You did not geuse the right number")
        print(f"you have {max_geuses-number_of_geuses} attempts remaining")
    else:
        print(f"OOOpps try another number the correct geuse number was {number_to_geuse}")    
        break