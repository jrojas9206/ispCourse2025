'''
Task

Write a Python terminal application to help you record N of your recipes in M recipe books.

When you run your script, you need to specify the number of recipes to store and the name of the book.
The book will be represented as a list of dictionaries. 
Each page of the book is defined as a dictionary with the keywords 'Title', 'Steps', 'Year'. 
If the book exists, the recipes must be loaded.

'''
import os 
import sys 
import json 
import argparse

def main():
    parser = argparse.ArgumentParser('A recipe app')
    parser.add_argument('nRecipes', type=int, help='Number of recipes you want to save')
    parser.add_argument('bookName', type=str, help='Book of recipes name')
    args = parser.parse_args()
    lstOfRecipies = []
    # The definition of this if is really correct? -- is redundant?
    if len(args.bookName)>0 and os.path.exists(f'{args.bookName}.json'):
        with open(f'{args.bookName}.json', 'r') as oFile:
            book = json.load(oFile)
        print(json.dumps(book, indent=4))
    else: 
        for nRecipe in range(args.nRecipes):
            print(f'Recipe Index: {nRecipe}')
            titleRecipe = input('What is the name of your recipe? ')
            dateRecipe = input('What is the date of creation of your recipe? ')
            stepsRecipe = input("Write the steps seprated by ',': " )
            steps = stepsRecipe.split(',')
            temporalDict = {}
            # Temporal dictionary
            temporalDict['title'] = titleRecipe
            temporalDict['steps'] = steps
            temporalDict['date'] = dateRecipe
            lstOfRecipies.append(temporalDict)
        # What happened if i use 'w' and not 'a'?
        with open(f'{args.bookName}.json', 'a') as fObje:
            json.dump(lstOfRecipies, fObje)
        print(json.dumps(lstOfRecipies, indent=4))
    return 0

if __name__ == '__main__':
    sys.exit(main())

'''
How to execute the script ?

python pyIntro_challenge_day1slide20.py 2 juices 

Recipe Index: 0
What is the name of your recipe? apple juice
What is the date of creation of your recipe? 2301
Write the steps seprated by ',': clean apple, remove apple skin, blend apple, drink apple juice
[
    {
        "title": "apple juice",
        "steps": [
            "clean apple",
            " remove apple skin",
            " blend apple",
            " drink apple juice "
        ],
        "date": "2301"
    }
]

A file juice.json is create representing the recipe book 
'''