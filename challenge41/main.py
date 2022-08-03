# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def calculate_primes(num):
    n = num
    i = 2
    factors = []
    while i <= n/2:
        if n % i != 0:
            i = i+1
        else:
            n = n/i
            factors.append(i)
    if n > 1:
        factors.append(int(n))
    print("The prime factorisation of number "+str(num)+" is:")
    print(*factors, sep=", ")


def prime_factorisation():
    exit = False
    while(exit !=True):
        num = input("Enter an integer to calculate its prime factors ( enter 0 for EXIT):")
        if num == "0":
            print("Exiting...")
            exit = True
        else:
            calculate_primes(int(num))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prime_factorisation()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
