# create a question
# create a delay with the time module
# create a list of answers
# generate a random number with the random module
# use taht random number to call the value of the index the list.

import time
import random
question = input("Please enter your question: ")

print ("thinking...")
time.sleep(3)

responses =[
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Definitely",
    "Don’t count on it",
    "Without a doubt",
    "Very doubtful",
    "It is certain",
    "Outlook not so good",
    "Signs point to yes",
    "Better not tell you now",
    "Yes, absolutely",
    "My sources say no",
    "You may rely on it",
    "Reply hazy, try again",
    "Concentrate and ask again",
    "Outlook good",
    "Most likely",
    "Cannot predict now"
]

response = random.randrange(0,21)
print(f"{responses[response]}")
    

