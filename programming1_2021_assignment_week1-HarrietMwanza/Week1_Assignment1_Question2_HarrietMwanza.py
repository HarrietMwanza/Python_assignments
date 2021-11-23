#What is Given
#Set a secret number
#User guesses the number
#Check if number matches the secret number
#If correct tell the user congratulations
#If not, check whether the number is above the secret number and tell the user number too high and vice versa
#Keep track of the number of guesses, same number guess counts as one guess.

#What is Required
#The user has to guess a secret number
#After every guess, the program tells the user whether their number was too large or too small.
#In the end, the number of tries needed should be printed.
#It counts only as one try if they input he same number multiple times consecutively

#The algorithm
#Initialize secret number
#Initialize attempts to 0
#While the guess is not equal to the secret number: Input user guess, if higher than the secret number, tell user number too high.
# If lower than the secret number, tell the user number too low.
#For every attempt, add 1 to attempts.
#When the guess and secret number matches, tell the user congratulations.
#Tell the user the number of attempts
