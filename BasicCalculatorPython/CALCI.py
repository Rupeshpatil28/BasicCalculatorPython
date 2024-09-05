print("Please Select Youre Problem :")

print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

progres = int(input("*_* =>"))

if progres == 1:
    num1 = int(input("Enter a First Number : "))
    num2 = int(input("Enter a Second Number  : "))
    print("Your Sum Is : ", num1 + num2)
elif progres == 2:
    num1 = int(input("Enter a First Number : "))
    num2 = int(input("Enter a Second Number : "))
    print("Your Diffrence is : ",num1 - num2)
elif progres == 3:
    num1 = int(input("Enter a First Number : "))
    num2 = int(input("Enter a Second Number : "))
    print("Your Answer : ",num1 * num2)
elif progres == 4:
    num1 = int(input("Enter a First Number : "))
    num2 = int(input("Enter a Second Number : "))
    print("Your OutPut : ",num1 / num2)
else:
    print("INVALID !")

