print "Please think of a number between 0 and 100!"

high = 100
low = 0
guess = (high + low)/2

print "Is your secret number", guess, "?"

while True: 
    
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if ans == "h":
        high = guess
        guess = (high + low)/2
        print "Is your secret number", guess, "?"
    elif ans == "l":
        low = guess
        guess = (high + low)/2
        print "Is your secret number", guess, "?"
    elif ans == "c":
        print "Game over. Your secret number was:", guess
        break
    else:
        print "Sorry, I did not understand your input."  
        print "Is your secret number", guess, "?"