'''### **1. Quote of the Day API**

**Concepts:** Flask routes, JSON response
**Goal:** Create a simple API that returns a random quote when `/quote` is visited.

**Subgoals:**

* Store quotes in a list or dictionary.
* Add a `/quotes` endpoint that returns all quotes.
* Let users submit new quotes via a POST request.
'''


from flask import Flask
import random

# name always contains the name of the current module
app = Flask(__name__)


quotes = [
"Success is not final; failure is not fatal; it is the courage to continue that counts.",
"Knowledge speaks, but wisdom listens.",
"The only limit to our realization of tomorrow is our doubts of today.",
"Simplicity is the ultimate sophistication.",
"Do not wait for the perfect moment; take the moment and make it perfect.",
"Well-done is better than well-said.",
"Action is the foundational key to all success.",
"Dream big and dare to fail.",
"Quality is not an act, it is a habit.",
"In the middle of difficulty lies opportunity."

]

@app.route('/quote')
def random_quote():
    print (" Quote of the day: \n")
    response = random.choice(quotes)
    return f"Quote of the day: {response}"
        

@app.route('/quotes')
def all_quotes():
    return "<br>".join(quotes)

@app.route('/add_quote/<new_quote>', methods=['POST'])
def add_quote(new_quote):
    quotes.append(new_quote)
    return f"New quote added: {new_quote}"


#When the file is run directly
if __name__ == '__main__':
    app.run(debug = True)
