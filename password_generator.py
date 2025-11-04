import random
import string
import sys

def checker():
        uppercase_choice = input("Include uppercase letters? (y/n): ").strip().lower()
        lowercase_choice = input("Include lowercase letters? (y/n): ").strip().lower()
        numbers_choice = input("Include numbers numbers? (y/n): ").strip().lower()
        symbols_choice = input("Include symbols letters? (y/n): ").strip().lower()

        return uppercase_choice, lowercase_choice, numbers_choice, symbols_choice 


def password_generator():
    i = 0
    password = []
    count=0
    while count<16:
        character = ["numbers","uppercase","lowercase","symbols"]
        character_choice = random.choice(character)

        if character_choice == "numbers" and numbers_choice == "y":
            numbers = random.randint(0,10)
            count += 1 
            password.append(numbers)
        elif character_choice == "uppercase" and uppercase_choice == "y":
            uppercase = random.choice(string.ascii_uppercase)
            count += 1 
            password.append(uppercase)
        elif character_choice == "lowercase" and lowercase_choice == "y":
            lowercase = random.choice(string.ascii_lowercase)
            count += 1 
            password.append(lowercase)
        elif character_choice == "symbols" and symbols_choice == "y":
            symbols = random.choice(["!","@","#","$","&"])
            count += 1 
            password.append(symbols)
    

    random.shuffle(password)
    print(f"\nGenerated Password: ", *password, sep="")
    print(f"Length: {len(password)}")
    print(f"contains: Uppercase letters? {uppercase_choice}, Lowercase letters? {lowercase_choice}, Numbers? {numbers_choice}, Symbols? {symbols_choice}")
    i+=1

    print()


uppercase_choice, lowercase_choice, numbers_choice, symbols_choice  = checker()

if uppercase_choice == "n" and lowercase_choice == "n" and numbers_choice == "n" and symbols_choice == "n":
    print("You must select at least one character type. Please try again.")
    sys.exit()
else:
    password_generator()


repeat = True
while repeat:
    user_input = input("Generate another password? (y/n) ").lower()
    
    if user_input == "y":
        checker()
        password_generator()
        
    else:
        repeat = False
        print("Thank you for using the password generator!")

