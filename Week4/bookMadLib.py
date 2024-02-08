import requests
import random

search_term = input("Enter a search term: ")
search_term = search_term.replace(" ", "+")
url = f"https://openlibrary.org/search.json?q={search_term}&limit=3" 

response = requests.request("GET", url)
 
status_code = response.status_code 
result = response.json()
print(result)
documents = result["numFound"] 

print("\n")
print(f"Amazing, I have found {documents} books for you!")
print("\n")
print(f"Here are the first 3 books: ")
print(result["docs"][0]["title"])
print(result["docs"][1]["title"])
print(result["docs"][2]["title"])
print("\n")

numOfBook = input("Which book would you like information on? ")
numOfBook = int(numOfBook) - 1
chosenBook = result["docs"][numOfBook]

print("\n")
print(f"Here is the information for {chosenBook['title']}: ")
print(f"Author: {chosenBook['author_name']}")
print(f"First Publish Year: {chosenBook['first_publish_year']}")
if("ratings_average" in chosenBook):
    print(f"Average Ratings: {chosenBook['ratings_average']}")
if("first_sentence" in chosenBook):
    print(f"First Sentence: {chosenBook['first_sentence']}")

wantMadLib = input("Would you like to create a MadLib with the characters in this book? (yes or no) ")
if wantMadLib == "yes":
    if "person" not in chosenBook:
        print("\n")
        print("I'm sorry, there are no characters in the record for this book.")
        print("\n")
    else:
        print("\n")
        print("Great! Let's create a MadLib with the characters in this book!")
        print("\n")
        numOfCharacters = len(chosenBook['person'])
        char1 = random.choice(chosenBook['person'])
        char2 = random.choice(chosenBook['person'])
        
        verb = input("Enter a verb: ")
        adj = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        print("\n")
        print(f"Once upon a time, {char1} and {char2} decided to {verb} to the {adj} {noun}.")
        print("\n")
        print("The end!")
else:
    print("\n")
    print("That's okay! Have a great day!")