# adds one to each digit without converting to string
# https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/

def addSingleDigits(number):
    number = int(number)
    index = 0
    newNumber = 0
    while number > 0:
        digit = number % 10
        newNumber += (digit + 1) * 10 ** index
        number = number // 10

        if digit == 9:
            index += 2
        else:
            index += 1
    return newNumber or 1
    
while True:
    try:
        num = int(input("input numbers: \n"))
        break
    except ValueError:
        print("only numbers accepted")

print(addSingleDigits(num))