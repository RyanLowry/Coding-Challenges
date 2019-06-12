## Performs the Havel-Hakimi algorithm
## https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

def removeZerosFromArray(arr):
    return [item for item in arr if item != 0]
def reverseArray(arr):
    arr.sort(reverse=True)
    return arr
def checkLength(num,arr):
    if num > len(arr):
        return True
    else:
        return False
def subtractFromArray(num,arr):
    for i in range(num):
        arr[i] -= 1
    return arr


def havelHakimi(arr):
    nonZeroArr = removeZerosFromArray(arr)
    if len(nonZeroArr) == 0:
        return True
    else:
        sortedArr = reverseArray(nonZeroArr)
        numToSubtract = sortedArr.pop(0)
        if checkLength(numToSubtract,sortedArr):
            return False
        else:
            finalArr = subtractFromArray(numToSubtract,sortedArr)
            return havelHakimi(finalArr)

while True:
    try:
        seq = input("input sequence of numbers seperated by commas: \n")
        seq = list(map(int,seq.split(',')))
        break
    except ValueError:
        print("Only input numbers seperated by commas")

isValidSequence = havelHakimi(seq)

print(isValidSequence)