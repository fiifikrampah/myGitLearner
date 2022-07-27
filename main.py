"""
A Simple python program to compute the Collatz Conjecture for a given number.
"""
# Store the Collatz numbers in a list
steps_list = []

# The app should only take positive numbers

# Function to compute the Collatz conjecture for a given number
def collatz(input_num):
    global steps_list
    # if input_num is even
    if input_num % 2 == 0:
        input_num = int(input_num / 2)
        steps_list.append(input_num)
        collatz(input_num)
    # else if input_num is odd and not 1
    elif (input_num % 2 == 1) and (input_num != 1):
        input_num = int((3 * input_num) + 1)
        steps_list.append(input_num)
        collatz(input_num)
    else:
        # end if input_num reaches 1
        pass
    # return the number of steps_list
    return len(steps_list)


def main():
    name = input("What is your name?")
    print("Welcome " + name)

    # Call the Collatz function with a value entered by the user
    number = input("Enter a positive number: ")
    result = collatz(int(number))
    print(
        f"The Collatz conjecture for the number you entered took: \
        {result} calculations"
    )
    print(f"The collatz list is: {steps_list}")


# Run program
main()
