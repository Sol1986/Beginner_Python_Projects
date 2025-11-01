a = int(input ("Enter side a: "))
b = int(input ("Enter side b: "))
c = int(input ("Enter side c: "))

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
        

print (pythagorean_triple_checker(a,b,c))


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