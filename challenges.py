#!/usr/bin/env python3

# 1.Write a Python function to find the Max of three numbers.
def maxOfThreeNum(num1:float, num2:float, num3:float):
    a = (num1,num2,num3)
    x = sorted(a,reverse=True)
    print(x[0])
maxOfThreeNum(2.1,5.7,9.6)

def maxOfThreeNum2(num1:float, num2:float, num3:float):
    a = (num1, num2, num3)
    x = max(a)
    print(x)
maxOfThreeNum2(2.1,5.7,9.6)

# 2.Write a Python function to sum all the numbers in a list.
def sumOfAll(num:list):
    sumNum = sum(num)
    print(sumNum)
sumOfAll([8,2,3,0,7])

# 3.Write a Python function to multiply all the numbers in a list.
def mult(nums:list):
    result = 1
    for num in nums:
        result = result * num
    print (result)
mult([8,2,3,-1,7])

# 5.Write a Python function to check whether a number is in a given range.
def numInRange(num:int,rangeMin:int=0, rangeMax:int=10):
    if (num >= rangeMin and num <= rangeMax):
        print(f"{num} is in the range {rangeMin} to {rangeMax}")
    else:
        print(f"{num} is not in the range {rangeMin} to {rangeMax}")

numInRange(12)
numInRange(5)


# 6.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def countUpperCase_LowerCase(sentence=str):
   chars=list(sentence)
   upperCount = 0
   lowerCount = 0
   for char in chars:
        if(char.isupper()==True):
            upperCount +=1
            print(upperCount)
        if (char.islower()==True):
            lowerCount +=1
            print(lowerCount)
   print(f"No. of Upper case characters : {upperCount}")
   print(f"No. of Lower case Characters : {lowerCount}")
countUpperCase_LowerCase("The quick Brow Fox")
