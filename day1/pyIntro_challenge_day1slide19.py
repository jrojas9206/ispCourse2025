'''
Task

Create a python application that helps you to study the multiplication tables from a to b

The script must request as execution arguments the table number e.g: 10, and as optional 
arguments the range of the multiplication table init=0, final=10

Look on internet the structure of argparse to manage the input arguments of the script 
Try your logic in the notebook but also try to prepare your python script .
'''
import sys  # Package to access some of the system parameters and functions 
import argparse #  Package to handle in a beautiful way the input args of the script


def main():
    parser = argparse.ArgumentParser('Multiplication table')
    parser.add_argument('--tableNumber', type=int, help='Multiplication table of a the n number. Default 5', default=5)
    parser.add_argument('--rangeInit', type=int, help='Initial number of the multiplication range to study. Default 0', default=0)
    parser.add_argument('--rangeFinal', type=int, help='Final number of the multiplication range to study. Default 10', default=10)
    args = parser.parse_args()

    '''
        'range' is a reserved word, this methods creates a list of element encapsulate on range object 
        range(3) = [0, 1, 2]
        range(1,3) = [1,2]
        range(1,4,2) = [1, 3] 
    '''

    for number in range(args.rangeInit, args.rangeFinal):
        print('---')
        multiplication = args.tableNumber * number
        print(f'{args.tableNumber} x {number} = {multiplication}')

    return 0

if __name__ == '__main__':
    sys.exit(main())

'''
How to run the code?

python pyIntro_challenge_day1slide19.py --tableNumber=5  --rangeInit=0 --rangeFinal=10

Output:

---
5 x 0 = 0
---
5 x 1 = 5
---
5 x 2 = 10
---
5 x 3 = 15
---
5 x 4 = 20
---
5 x 5 = 25
---
5 x 6 = 30
---
5 x 7 = 35
---
5 x 8 = 40
---
5 x 9 = 45

Challenge 

How will you modify this piece of code to give the user more operations options [+, -, /]?
'''