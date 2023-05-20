import unittest
# given a string consisting of the letters x and y, such as xyxxxyxyy. 
# In addition, you have an operation called flip, 
# which changes a single x to y or vice versa.
# 
# Determine how many times you would need to apply this operation to ensure that all x's come before all y's.
# In the preceding example, it suffices to flip the second (1st position) and sixth (5th position) characters, so you should return 2.


# solution to the prompt above
def numToFlip(value):
    newInd = 0
    # reverse the string to get number of trailing y's
    for ind,i in enumerate(reversed(value)):
        # this would return the index off by 1 since it stops at first x and not last y, and to make sure it is at least 1 and not 0 when slicing the string.
        if i == 'x':
            newInd = ind + 1
            break
    ## return the count of the sliced string not including trailing y's
    return value[:-newInd].count("y")

# logic incase we want to know the index positions of the y's instead of just the number of them
def countYAndPositions(value):
    yPositions = []
    newInd = 0
    for ind,i in enumerate(value):
        # resets the last y values to find trailing y's
        if i == 'x':
            newInd = 0
        else:
            yPositions.append(ind)
            newInd += 1
    # slicing string/arrays with 0 would cause incorrect values, a check in case an x is at the end of the string
    if newInd == 0:
        yCount = value.count("y")
    else:
        yCount = value[:-newInd].count("y")
        # we don't want the trailing y's so we remove them from the array
        yPositions = yPositions[:-newInd]
    return [yPositions,yCount]

class TestFlipStrings(unittest.TestCase):
    def test_example(self):
        string = "xyxxxyxyy"
        self.assertEqual(numToFlip(string), 2)
        self.assertEqual(countYAndPositions(string), [[1,5],2])
        
    def test_noTrailing(self):
        string = "xxyxyxxyxxyx"
        self.assertEqual(numToFlip(string), 4)
        self.assertEqual(countYAndPositions(string), [[2,4,7,10],4])
    
    def test_noChange(self):
        string = "xxxxyyy"
        self.assertEqual(numToFlip(string), 0)
        self.assertEqual(countYAndPositions(string), [[],0])
        
    def test_grouping(self):
        string = "yyxxxyxyyyxxy"
        self.assertEqual(numToFlip(string), 6)
        self.assertEqual(countYAndPositions(string), [[0,1,5,7,8,9],6])

if __name__ == '__main__':
    unittest.main()