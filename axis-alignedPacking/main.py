#Program that determines how many boxes can fit in a crate, fit1,fit2,fit3, O(N!) solution fitn
#https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

from itertools import permutations as permutations
def fit1(X,Y,x,y):
    # // Integer division
    xAxis = X // x
    yAxis = Y // y
    return xAxis * yAxis

def fit2(X,Y,x,y):
    newX = fit1(X,Y,x,y)
    newY = fit1(X,Y,y,x)
    return max([newX,newY])

def f3(X,Y,Z,x,y,z):
    xAxis = X // x
    yAxis = Y // y
    zAxis = Z // z
    return xAxis * yAxis * zAxis
def fit3(X,Y,Z,x,y,z):
    axis1 = f3(X,Y,Z,x,y,z)
    axis2 = f3(X,Y,Z,y,x,z)
    axis3 = f3(X,Y,Z,z,y,x)
    axis4 = f3(X,Y,Z,y,z,x)
    axis5 = f3(X,Y,Z,z,x,y)
    axis6 = f3(X,Y,Z,x,z,y)
    return max([axis1,axis2,axis3,axis4,axis5,axis6])

def fn(axisArr,boxArr):
    axisValue = 1
    for i in range(len(boxArr)):
        axisValue *= axisArr[i] // boxArr[i]
    return axisValue

def fitn(crateArr, boxArr):
    permutationValues = permutations(boxArr)
    boxes = []
    for boxPerm in permutationValues:
        newBox = fn(crateArr,boxPerm)
        boxes.append(newBox)
    return max(boxes)

print(fit1(25, 18, 6, 5)) # 12
print(fit2(25, 18, 6, 5)) # 15
print(fit3(12, 34, 56, 7, 8, 9)) #32
print(fitn([123, 456, 789], [10, 11, 12])) #32604