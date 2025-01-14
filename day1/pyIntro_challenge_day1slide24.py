'''
Task 

Create a Python application to help you calculate the area of different geometries.  
[Each geometry must have his own method]

E.g: 
    - square 
    - Circle 
    - Triangle 

Use the knowledge you have just acquired to create an infinite menu. 
[The menu must also be a method... Is it possible to pass the N range 
method to the menu method as an argument?]

'''

import os 
import sys  
import argparse 
from math import pi

def squareArea(side:float) -> float:
    '''
        Get the square area

        Parameters
        -----------
            side : float, Lenght of one sides square 

        Returns 
        --------
            float 
                Square area 
    '''
    return side*side

def circleArea(radius:float) -> float:
    '''
        Calculate the circle area 

        Parameters 
        -----------
            radius : float, Cricle's radius 

        Return 
        -------
            float 
                cricle area     
    '''
    return pi*radius**2

def main():
    parser = argparse.ArgumentParser('Area calculator script')
    parser.add_argument('--radius', type=float, help='Radius of the circle')
    parser.add_argument('--sideLength', type=float, help='Lenght of one side of the square')
    parser.add_argument('--isCircle', help='Calculate the circle area', action='store_true')
    parser.add_argument('--isSquare', help='Calculate the square area', action='store_true')
    args = parser.parse_args()

    if args.isCircle and not args.isSquare:
        print(f'Circle with radius {args.radius} has an area of :{circleArea(args.radius)}')
    elif not args.isCircle and args.isSquare:
        print(f'Square with a length of {args.sideLength} has an area of :{squareArea(args.sideLength)}')
    else:
        raise ValueError('Options were selected in a unexpected way!')
    return 0 

if __name__ == '__main__':
    sys.exit(main())

'''
    How to use it ?

    - python pyIntro_challenge_day1slide24.py --isCircle --radius 5 

        Circle with radius 5.0 has an area of :78.53981633974483

    - python pyIntro_challenge_day1slide24.py --isSquare --sideLength 5 

        Square with a length of 5.0 has an area of :25.0
    
    - python pyIntro_challenge_day1slide24.py --isSquare --radius 5     

        How to fixe this error? 
        
Traceback (most recent call last):
  File "C:\Users\J.Bustos\Documents\isp2025\pyIntro_challenge_day1slide24.py", line 70, in <module>
    sys.exit(main())
             ^^^^^^
  File "C:\Users\J.Bustos\Documents\isp2025\pyIntro_challenge_day1slide24.py", line 64, in main
    print(f'Square with a length of {args.sideLength} has an area of :{squareArea(args.sideLength)}')
                                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\J.Bustos\Documents\isp2025\pyIntro_challenge_day1slide24.py", line 36, in squareArea
    return side*side
           ~~~~^~~~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
'''