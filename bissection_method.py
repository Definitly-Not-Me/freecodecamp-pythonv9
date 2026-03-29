"""Implement the Bisection Method

The bisection method, also known as the binary search method, uses a binary search to find the roots of a real-valued function. It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

For example, if the tolerance is 0.01, the bisection method will keep halving the interval until the difference between the upper and lower bounds is less than or equal to 0.01.

In this lab, you will implement a function that uses the bisection method to find the square root of a number.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

    You should define a function named square_root_bisection with three parameters:
        The number for which you want to find the square root.
        The tolerance being the acceptable error margin for the result. You should set a default tolerance value.
        The maximum number of iterations to perform. You should set a default number of iterations.

    The square_root_bisection function should:
        Raise a ValueError with the message Square root of negative number is not defined in real numbers if the number passed to the function is negative.
        For numbers 0 and 1, print the message: The square root of [number] is [number] and return the number itself as the square root.
        For any other positive number, print the approximate square root with the message: The square root of [square_target] is approximately [root] and return the computed root value.
        If no value meets the tolerance condition, print a failure message: Failed to converge within [maximum] iterations and return None.

Note: You cannot import any module for this lab.
"""
from random import random, randint
def square_root_bisection(number :float, tolerance: float = 0.01, maximum: int= 200)-> float:
    ##check for special case
    if number < 0:
        #A ne pas supprimer !!
        raise ValueError("Square root of negative number is not defined in real numbers")
        return None
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
                
    low = 0
    high = number if number > 1 else 1
    f_high = high**2 - number 
    mid = (high + low)/2
    
    print(f"Initialisation : \n *number = {number} \n *tolerance = {tolerance} \n *maximum = {maximum} \n")
    for i in range(maximum):
        print(f"#Pour c = {mid}")
        #Soit f(x) = x**2 - number. sqrt(number) est une racine de f
        f_mid = mid**2 - number

        if high - low <= tolerance:
            print(f"{high} - {low} <= tolerance ---> sqrt({number}) ~ {mid}!!")
            print(f"The square root of {number} is approximately {mid}")
            return mid
        
        if (f_high > 0) and (f_mid > 0):
            high = mid
            f_high = f_mid            
        else:
            low = mid
        
        mid = (low + high)/2
            
           
        
    print(f"Failed to converge within {maximum} iterations")
    return None

#test = [randint(1, 100) for _ in range(10)]
#toler = [random() for i in range(10)] 
#maximum_iter = [round(randint(1, 100)*random()) for i in range(10)]
#result = [square_root_bisection(test[i], toler[i], maximum_iter[i]) for i in range(10)]
#print(result)

print(square_root_bisection(0.001, 1e-7, 50))