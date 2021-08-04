def collatz(num):
    # if num is even
    while (num > 1):
        if num % 2 == 0:
            num = num / 2 
            return(num)
        # else num is odd
        else:
            num = (3 * num) + 1
            return(num)

collatz(10)

# Eddy complete the following code here:

def mainFunc():
    print("What is your name?") 
    print("My name is Fiifi") 
    # Change line 18 to print your name

    # Call the collatz function with a value entered by the user
    number = input("Enter a positive number: ")
    result = collatz(int(number))
    print(result)

mainFunc()
