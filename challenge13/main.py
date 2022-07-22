# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_index_by_letter(letter):
    letter_index = -1;
    for index, letter_in_alphabet in enumerate(alphabet):
        if letter == letter_in_alphabet:
            letter_index = index
    return letter_index


def get_shifted_index(index, key):
    shifted_index = index + key
    if shifted_index > 25:
        shifted_index = shifted_index - 26
    elif shifted_index < 0:
        shifted_index = shifted_index + 26
    return  shifted_index

def cypher_letter(letter, key):
    index = get_index_by_letter(letter)
    shifted_index = get_shifted_index(index, key)
    print("The letter is ", letter, " the key is ", key, " shifted index is ", shifted_index, " new letter is ", alphabet[shifted_index])
    return alphabet[shifted_index]

def decypher_letter(letter, key):
    return cypher_letter(letter, key*-1)


def cypher_word(word, key):
    new_word = "";
    for letter in word:
        new_word+=cypher_letter(letter, key)
    print("The word is ", word, " the key is ", key, " encoded word is: ", new_word)

def decypher_word(word, key):
    return cypher_word(word, key*-1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cypher_word("apple", 2)
    decypher_word("crrng", 2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
