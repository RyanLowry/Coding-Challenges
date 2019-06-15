# recursive function of additive Persistence
# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

def additivePersistence(number,level = 1):
    summedValue = 0
    while number > 0:
        digit = number % 10
        summedValue += digit
        number = number // 10
    if summedValue > 9:
        return additivePersistence(summedValue,level + 1)
    else:
        return level

while True:
    try:
        num = int(input("input numbers: \n"))
        break
    except ValueError:
        print("only numbers accepted")

print(additivePersistence(num))
