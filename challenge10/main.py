ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["", "one hundred and", "two hundred and", "three hundred and", "four hundred and", "five hundred and"]



def print_number(n):
    if(n) < 10:
        print(ones[n])
    elif (n >= 10) and (n < 20):
        print(teens[n-10])
    elif(n >= 20) and (n < 100 ):
        temp = [int(d) for d in str(n)]
        # 39 => temp[0]=3, temp[1]=9
        print(tens[temp[0]] +" "+ ones[temp[1]])
    elif(n >= 100) and (n < 1000 ):
        temp = [int(d) for d in str(n)]
        print(hundreds[temp[0]] +" "+ tens[temp[1]] + " "+ ones[temp[2]])


def start():
    number = 101
    print_number(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

