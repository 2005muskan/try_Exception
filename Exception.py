print("enter a first value : ")
num1= int(input())

print("enter a second value : ")
num2 = (input())

try:
    print("sum of num1 + num2 :  ",num1 + num2)
except Exception as s:
    print("hello")


print("==================================")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("nothing !!!....")
  