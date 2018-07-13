## Applies knuth up arrow notation
## https://www.reddit.com/r/dailyprogrammer/comments/8xbxi9/20180709_challenge_365_easy_uparrow_notation/

def knuthArrows(base, length, exp):
    result = base
    if length == 1:
        return base ** exp
    for i in range(1, exp):
        #example 2 ^^^ 3
        ## will result in 2 ^^ 2, recurse until one ^ is reached
        result = knuthArrows(base, length - 1, result)
    return result

userInput = input("Enter value and exponents: ").split(" ")
print(knuthArrows(int(userInput[0]),len(userInput[1]),int(userInput[2])))