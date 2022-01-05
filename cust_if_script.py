#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'The letter grade associated with the score you entered is: '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your numeric score?"))


if score >= 90 and score <=100:
    message = message + 'A.'
elif score >= 80 and score <= 89:
    message = message + 'B.'
elif score >= 70 and score <=79:
    message = message + 'C.'
elif score >=60 and score <=69:
    message = message + 'D.'
elif score <=59:
    message = message + 'F.'
else:
    message = 'The score you entered is invalid. Please enter number between 0 and 100.'
print(message)

