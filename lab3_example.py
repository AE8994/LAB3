############################################################
#   Purpose: Lab 3 program to demonstrate concepts learned
#           in chapter 3. Determine the secondary by mixing
#           two primary colors (red, yellow, blue) selected
#           by the user.
#
#   AUTHOR: Adrian Edmundson
#   Written: 9/18/2024
#   Version 1.0.0
#
############################################################

# Named Constants
# Primary colors
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'
# Secondary colors
GREEN = 'green'
PURPLE = 'purple'
ORANGE = 'orange'

# Boolean Flag
isValid = False

# Print some instructions for the user
print('Welcome to the Color Mixer program.\n')
print('Primary colors are red, yellow, and blue.')
print('You will select two primary colors to find the secondary color.\n')
# Get the first primary color from the user
color1 = input('Enter the first primary color.')
print(f'You enter {color1} for the first primary color.')
# Get the second primary color from the user
color2 = input('Enter the second primary color.')
print(f'You enter {color2} for the second primary color.')


# Determine the secondary color
if color1 == color2:
    print(f'\nYou entered {color1} and {color2}.')
    print('You entered the same color for the first and second color.')
elif (color1.lower() == RED and color2.lower() == BLUE) or \
   (color1.lower() == BLUE and color2.lower() == RED):
    isValid = True  # valid colors, set the flag to True
    result = PURPLE
elif (color1.lower() == RED and color2.lower() == YELLOW) or \
   (color1.lower() == YELLOW and color2.lower() == RED):
    isValid = True  # valid colors, set the flag to True
    result = ORANGE
elif (color1.lower() == BLUE and color2.lower() == YELLOW) or \
   (color1.lower() == YELLOW and color2.lower() == BLUE):
    isValid = True  # valid colors, set the flag to True
    result = GREEN
else:
    print(f'\nYou entered {color1} and {color2}.')
    print('One of these colors is an invalid primary color.')
    

# Display the resulting secondary color
if isValid:
    print(f'\nYou entered {color1} and {color2} and the secondary color is {result}.')
else:
    print('There was an error during processing.')

print('\nThank you for using the Color Mixer program.')



