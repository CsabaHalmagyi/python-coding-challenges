

morseCode = {"A":".-","B":"-...","C":"-.-."}
morseCode["D"] = "-.."
morseCode["E"] = "."
morseCode["F"] = "..-."
morseCode["G"] = "--."
morseCode["H"] = "...."
morseCode["I"] = ".."
morseCode["J"] = ".---"
morseCode["K"] = "-.-"
morseCode["L"] = ".-.."
morseCode["M"] = "--"
morseCode["N"] = "-."
morseCode["O"] = "---"
morseCode["P"] = ".--."
morseCode["Q"] = "--.-"
morseCode["R"] = ".-."
morseCode["S"] = "..."
morseCode["T"] = "-"
morseCode["U"] = "..-"
morseCode["V"] = "...-"
morseCode["W"] = ".--"
morseCode["X"] = "-..-"
morseCode["Y"] = "-.--"
morseCode["Z"] = "--.."
morseCode[" "] = " "

def text_to_morse():
    userInput = input("Enter a sentence to be encrypted into morse code:")
    morseText = ""
    for char in userInput:
        if char.upper() in morseCode:
            morseText += morseCode[char.upper()] + "|"
        else:
            morseText += " " + "|"
    print(morseText)

def morse_to_text():
    print()

def morse_code_menu():
    exit = False
    while(exit !=True):
        option = input("Select an option (1-Text to morse code, 2-Morse code to text, 3-EXIT):")
        if option == "1":
            text_to_morse()
        elif option == "2":
            morse_to_text()
        elif option == "3":
            print("Exiting...")
            exit = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    morse_code_menu()

