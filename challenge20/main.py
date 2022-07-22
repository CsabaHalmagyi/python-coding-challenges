# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def is_palindrome(str):
    reverse = ""
    for i in range(len(str)-1, -1, -1):
        reverse += str[i]

    if str == reverse:
        print("The word ", str, " is a palindrome:", reverse)
    else:
        print("The word ", str, " is not a palindrome:", reverse)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_palindrome("apple")
    is_palindrome("racecar")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
