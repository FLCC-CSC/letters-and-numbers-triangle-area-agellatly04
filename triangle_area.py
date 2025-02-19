# FILE NAME - triangle_area.py
# DRG - Rerun for points 2025-02-18-2343
# NAME: Andrew Gellatly   
# DATE: 2/18/2025
# BRIEF DESCRIPTION:  a program that calculates the area of a triangle based on user input.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########
    
height = float(input('Enter the height: '))
base = float(input('Enter the base: '))
area = float(0.5 * height * base)

print()
print(f'The area of the triangle is {area}')
    
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?

I started by defining my variables based on user input, calculated the triangle area, and displayed it.



2. What was the hardest part of this lab?

I figured out I had to use 'float' instead of 'double' in Python.



'''
