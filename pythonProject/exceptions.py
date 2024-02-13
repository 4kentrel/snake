try:
    print(x)
except:
    print("NameError occurred")
finally:
    print("success")
try:
    num1 = 20
    num2 = 5
    print(num1 / num2)
except:
    print("Error occured")
finally:"success"
#User-defines function
try:
    def sum(first, second):
        return first + second
except:print("Error")
finally:"success"
print(sum(10,20))
