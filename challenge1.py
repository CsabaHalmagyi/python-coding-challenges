

def recur_factorial(num):
   if num == 1:
       return num
   else:
       return num*recur_factorial(num-1)

def factorial_without_loop(num):
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

def factorial_with_loop(num):
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


if __name__ == '__main__':
    factorial_with_loop(5)