bemsg = "To pop a bubble press 'a'"
end = "All bubbles popped! press 'e' to try again or any other key to exit."
PopsLeft = 12
oops = "You didn't press 'a'! Try again."
oops2 = "Thanks for playing!"

## Prints in the Termal the beggining message with what to type
print(bemsg)

##Function that checks if 'a' was entered to print out the pop message
def press_a():
    global PopsLeft
    if input() == 'a':
        PopsLeft -= 1
        print(f"POP you have {PopsLeft} left to pop!")
    else:
        print(oops)

##Checks if they poped more than 12 bubbles and if so, prints the end message
def check_pops():
    while PopsLeft > 0:
        press_a()
    else:
        print(end)

check_pops()

##Checks if the user wants to play again or exit the game
while PopsLeft == 0:
    if input() == 'e':
        PopsLeft = 12
        print(bemsg)
        check_pops()
    else:
        print(oops2)
        break
