import json
from difflib import get_close_matches

data = json.load(open("data.json"))

#for searching every possible word if exact word not found in dict
def possibleWords(key):
    for value in get_close_matches(key,data.keys()):
        possible = input("Do you mean "+ "'"+ value +"'"+" if yes(Y) else no(N): ")
        if possible == "Y":
            return dictSearch(value)
        elif possible == "N":
            continue
        else:
            input("Please enter valid input, if yes(Y) else no(N): ")
    return print("Sorry not found in dict. Please enter right word")

#class for searching a given key
def dictSearch(key):
    if key in data:
        count = 1
        for ans in data[key]:
        
            print(str(count) + ". " + ans)
            count += 1
    else:
        #charset = list(key)
        return possibleWords(key)

key= input("Enter the word : ")
key = key.lower()

dictSearch(key)