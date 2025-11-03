# Pythagorean Triples Checker
def pythagorean_triple_checker(x,y,z):
    if (x**2 + y**2) == z**2:
        message = f"\n{x},{y},{z} are a Pythagorean Triple\n"
        
    elif (x**2 + z**2) == y**2:
        message = f"\n{x},{y},{z} are a Pythagorean Triple\n"
        
    elif (y**2 + z**2) == x**2:
        message = f"\n{x},{y},{z} are a Pythagorean Triple\n"
        
    else:
        message = f"\n{x},{y},{z} are not a Pythagorean Triple\n"
    
    return message

# Function to get sides from user
def get_sides():
    side_a = int(input ("Enter side a: "))
    side_b = int(input ("Enter side b: "))
    side_c = int(input ("Enter side c: "))

    return side_a,side_b,side_c

a,b,c = get_sides()
print (pythagorean_triple_checker(a,b,c))
        
play_again = True

# Loop to allow multiple checks
while play_again:
    
    question = input ("Play again? (y/n): ")
    
    if question == "y" or question =="Y":
        a,b,c = get_sides()
        print (pythagorean_triple_checker(a,b,c))
    elif question == "n" or question =="N":
        play_again = False
    else:
        print ("wrong input.")



print ("Thanks for playing.")


# Notes:
# print(robot.name)     # prints a stored value
# print(robot.speak())  # runs code inside the speak() function



'''
# another version without return statement
def pythagorean_triple_checker(x, y, z):
    if (x**2 + y**2) == z**2:
        print(f"{x},{y},{z} are a Pythagorean Triple")
    elif (x**2 + z**2) == y**2:
        print(f"{x},{y},{z} are a Pythagorean Triple")
    elif (y**2 + z**2) == x**2:
        print(f"{x},{y},{z} are a Pythagorean Triple")
    else:
        print(f"{x},{y},{z} are not a Pythagorean Triple")

pythagorean_triple_checker(a, b, c)
'''