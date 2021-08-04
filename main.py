# Store the collatz numbers in a list
steps = []
def collatz(num):
    global steps
    # if num is even
    if num % 2 == 0:
        num = int(num / 2)
        steps.append(num)
        collatz(num)
    # else if num is odd and not 1
    elif (num % 2 == 1) and (num != 1):
        num = int((3 * num) + 1)
        steps.append(num)
        collatz(num)
    else:
        # end if num reaches 1
        pass
    # return the number of steps
    return(len(steps))


def mainFunc():
    name=input("What is your name?") 
    print("Welcome" + name) 

    # Call the collatz function with a value entered by the user
    number = input("Enter a positive number: ")
    result = collatz(int(number))
    print(f"The collatz conjecture for the number you entered took: {result} calculations")
    print(f"The collatz list is: {steps}")

mainFunc()
    
    

    # Change line 18 to print your name
