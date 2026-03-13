num1=float(input("digit the first number"))
num2=float(input("the second"))
operation=input("choose an operation: 1 it's summing, 2 it's subtraction, 3 is multiplication, 4 is division.")
if operation=="1":
  print(num1+num2)
elif operation=="2":
  print(num1-num2)
elif operation=="3":
  print(num1*num2)
elif operation=="4":
  print(num1/num2)
else:
  print("no found operation, try again.")
