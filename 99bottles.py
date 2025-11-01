# Create a program that prints the lyrics to the song "99 Bottles of Beer on the Wall".
# The program should count down from 99 to 0, printing the appropriate lyrics for each verse.
# When the count reaches 0, the program should print a final verse indicating that there are no more bottles left.
# Do not use a list of numbers or type it in manually. use a function instead 
# beside the phrase take one down 
# when 1 bottle left, bottle not bottles.

# Process
# we need to make a function that loops for 99 rounds. 
# it basically has variables for where the numbers go. One of the numbers is i and the other is i-1

count= 99
while count>=0:
    
    if count>1:
        print(f"{count} bottles of beer on the wall, {count} bottles of beer.\nTake one down and pass it around, {count-1} bottles of beer on the wall.")
    elif count==1:
        print(f"{count} bottles of beer on the wall, {count} bottles of beer.\nTake one down and pass it around, {count} bottle of beer on the wall.")
    else:
        print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
    
    count -=1