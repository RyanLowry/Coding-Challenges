import re
import time

## Creats hyphens between a word based on a pattern algorithm
## https://www.reddit.com/r/dailyprogrammer/comments/8qxpqd/20180613_challenge_363_intermediate_word/

def getMatches(pattern,word):
    con = re.sub(r'[0-9.]+',"",pattern)
    if pattern[0] is ".":
        if word.startswith(con):
            return pattern
    elif pattern[-1] is ".":
        if word.endswith(con):
            return pattern
    elif con in word:
        return pattern

def applyNumbers(positionDict,word):
    # Don't enumerate because we don't count numbers for index
    count = 0
    for letter in word:
        # Validate existence of key
        if letter.isdigit():
            if count in positionDict:
                positionDict[count].append(letter)
            else:
                positionDict[count] = [letter]
            count -= 1
        count += 1
    return positionDict

def applyHyphen(word,patternMatches):

    orderedPattern = []
    stripped = [re.sub(r'[0-9.]+',"",pattern) for pattern in patternMatches]
    ignoreList = []
    finalWord = ""
    letters = ""
    positionDict = {}
    i = 0
    while i < len(word):
        #checks pattern between every added letter, going back to 0 if match is found
        letters += word[i]
        for index,strip in enumerate(stripped):
            if strip in letters and strip not in ignoreList:
                orderedPattern.append(pattern)
                finalWord = word.replace(strip,patternMatches[index])
                
                positionDict = applyNumbers(positionDict,finalWord)

                letters = ""
                i = 0
                ignoreList.append(strip)
                finalWord = word
                continue
        i += 1
    # Add offset for when loop converts numbers to dashes
    offset = 0
    for i,letter in enumerate(word):
        if i in positionDict:
            maxValue = max(positionDict[i])
            if int(maxValue) % 2 != 0:
                finalWord = finalWord[:i + offset] + "-" + finalWord[offset + i:]
                offset += 1
    return finalWord

# the word patterns for hyphens
with open('tex-hyphenation-patterns.txt', 'r') as f:
    patterns = [word.strip() for word in f.readlines()]
word = input()
patternMatches = []


for pattern in patterns:
    matched = getMatches(pattern,word)
    if matched is not None:
        patternMatches.append(matched)
startTime = time.time()
finalWord = applyHyphen(word,patternMatches)
print(finalWord)
print(time.time() - startTime)