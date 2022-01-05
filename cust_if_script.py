#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A program that prompts a user for a numeric score, then returns the letter grade associated with that score."""


message = 'The letter grade associated with the score you entered is: '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your numeric score?"))

if score >100 or score <0:
    message = 'The score you entered is invalid. Please enter number between 0 and 100.'

elif score >= 90 and score <= 100:
    message = message + 'A.'
elif score >= 80:
    message = message + 'B.'
elif score >= 70:
    message = message + 'C.'
elif score >= 60:
    message = message + 'D.'
else:
    message = message + 'F.'

print(message)

