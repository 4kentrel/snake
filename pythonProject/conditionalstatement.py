temperature = 34
if temperature > 25:
    print("hot")
else:print("cold")

#A program that determines the largest number among 3 numbers
num1 = 47
num2 = 32
num3 = 77
if num1 > num2 and num1 < num3:
    print("num3 is the largest number")
elif num2 > num1 and num2 < num3:
    print("num2 is the second largest number")

#A program that checks whether a number is even or odd
number = 12
if number % 2 == 0:
    print(number,"is even")
else:
    print(number,"is odd")
number = 47
if number > 1 :
    for x in range(2,number):
        if number % x == 0:
         print("Not prime")
        else:print("Is prime")
        break
else:
    print("is not a prime number")



