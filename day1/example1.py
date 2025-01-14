import argparse
import json
import sys  

def main():
    parser = argparse.ArgumentParser('A recipe app')
    parser.add_argument('nRecipes', type=int, help='Number of recipes you want to save')
    parser.add_argument('bookName', type=str, help='Book of recipes name')
    args = parser.parse_args()
    lstOfRecipies = []
    for nRecipe in range(args.nRecipes):
        print(f'Recipe Index: {nRecipe}')
        titleRecipe = input('What is the name of your recipe?')
        dateRecipe = input('What is the date of creation of your recipe?')
        stepsRecipe = input("Write the steps seprated by ',':" )
        steps = stepsRecipe.split(',')
        temporalDict = {}
        # Temporal dictionary
        temporalDict['title'] = titleRecipe
        temporalDict['steps'] = steps
        temporalDict['date'] = dateRecipe
        lstOfRecipies.append(temporalDict)
    with open(args.bookName, 'a') as fObje:
        json.dumps(fObje, lstOfRecipies)

    return 0

if __name__ == "__name__":
    sys.exit(main())