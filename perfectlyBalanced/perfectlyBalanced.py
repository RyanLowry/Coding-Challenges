# A program that checks if every letter appears same number of times.
# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

# function that only checks x and y balance
def balanced(values):
    if len(values) % 2 == 0:
        x,y = 0,0
        for val in values:
            if val == "x":
                x += 1
            elif val == "y":
                y += 1
        if (x == y):
            return True
    return False

# function that checks every letter balance
def balanced_bonus(values):
    letters = {}
    for val in values:
        if val in letters:
            letters[val] += 1
        else:
            letters[val] = 0
    value_list = list(letters.values())
    return all(x == value_list[0] for x in value_list)
