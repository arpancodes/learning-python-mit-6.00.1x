'''
 The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
 The computer makes guesses, and you give it input - is its guess too high or too low?
 Using bisection search, the computer will guess the user's secret number!
'''

high = 100
low = 0
ans = int((high+low)/2)

while True:
    answer = input("is your secret number " + str(ans) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == "h":
        high = ans
        ans = int((high+low)/2)
    elif answer == "l":
        low = ans
        ans = int((high+low)/2)        
    elif answer == "c":
        print("Game over. Your secret number was: " + str(ans))
        break
    else: 
        print("\nSorry, I did not understand your input.")
