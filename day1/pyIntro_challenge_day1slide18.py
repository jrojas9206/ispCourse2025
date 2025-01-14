'''
Task : Can you calculate the sum of numbers from 0 till N
'''
import argparse # Package to handle in a beautiful way the input args of the script
                # I advise in general to use this packages as latter on it will help you 
                # to control in a better way the parameters and testing of your script
'''
In Python there is no need to define a main method,
it can be executed directly as it is done in this script.

However, it is recommended to add a main method to know where 
is the core of the project. 
'''

parser = argparse.ArgumentParser('Simple sum of numbers')
parser.add_argument('n', type=int, help='Sum the number from 0 till n')
args = parser.parse_args()

number = args.n+1 # Why do I added 1 here?
varSum = 0 # Variable that will contain the sum of all the elements 

for currentNumber in range(1, number):
    varSum = varSum + currentNumber
    print('----')
    print(f'Current number to be added: {currentNumber}')
    print(f'Current value of the addition: {varSum}')

'''
How to execute the script?

python pyIntro_challenge_d1s18.py 3

Output:

----
Current number to be added: 1
Current value of the addition: 1
----
Current number to be added: 2
Current value of the addition: 3
----
Current number to be added: 3
Current value of the addition: 6
'''

