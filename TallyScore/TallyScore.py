from operator import itemgetter

# A program that tallies single character inputs depending on upper or lower case.
# https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/

def tally(value):
    scores = {}
    for ch in value:
        if not ch.lower() in  scores:
            scores[ch.lower()] = 0
        if ch.isupper():
            scores[ch.lower()] = scores[ch.lower()] - 1
        else:
            scores[ch] = scores[ch] + 1
    return scores

if __name__ == "__main__":
    inputString = input("Enter values:")
    answer = tally(inputString)
    print(sorted(answer.items(),key = itemgetter(1),reverse = True))