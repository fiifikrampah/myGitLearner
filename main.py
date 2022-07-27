"""
A Simple python program to compute the Collatz Conjecture for a given number.
"""
# Store the collatz numbers in a list
steps = []

# The app should only take positive numbers

# Function to compute the collatz conjecture for a given number
def collatz(number):
    global steps
    # if number is even
    if number % 2 == 0:
        number = int(number // 2)
        steps.append(number)
        collatz(number)
    # else if number is odd and not 1
    elif (number % 2 == 1) and (number != 1):
        number = int((3 * number) + 1)
        steps.append(number)
        collatz(number)
    else:
        # end if number reaches 1
        print("The number has reached 1!")
        pass
    # return the number of steps
    return len(steps)


def main():
    name = input("What is your name?")
    print("Welcome " + name)

    # Call the collatz function with a value entered by the user
    number = input("Enter a positive number: ")
    result = collatz(int(number))
    print(
        f"The collatz conjecture for the number you entered took: \
        {result} calculations"
    )
    print(f"The collatz list is: {steps}")


# Run program
main()
