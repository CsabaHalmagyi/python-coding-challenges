# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def vat_calculator():
    print("VAT calculator")
    price = input("Enter the price of a product to calculate VAT:")
    vat = float(price)*0.20
    print("The 20% VAT is: "+str(vat))


def tax_calculator():
    print("Tax calculator")
    salary = input("Enter your salary to calculate tax:")
    tax = float(salary)*0.25
    print("The tax on your salary is: "+str(tax))

def timestable_calculator():
    print("Timestable calculator")


def life_calculator():
    exit = False
    while(exit !=True):
        option = input("Select a calculator option (1-VAT, 2-TAX, 3-Times table, 4-EXIT):")
        if option == "1":
            vat_calculator()
        elif option == "2":
            tax_calculator()
        elif option == "3":
            timestable_calculator()
        elif option == "4":
            print("Exiting...")
            exit = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    life_calculator()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
