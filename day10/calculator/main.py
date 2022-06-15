from art import logo
print(logo)

def add(a,b):
  return(a+b)
def subtract(a,b):
  return(a-b)
def multiply(a,b):
  return(a*b)
def divide(a,b):
  if (b!= 0):
    return(a/b)
  else:
    return("Invalid Input")

check_end  = 0
num1 = int(input("Enter a number: "))
operator ={
  "+": add,
  "*": multiply,
  "-": subtract,
  "/": divide
}
for operation in operator:
    print (operation)

while (check_end == 0):
  op = input("Enter the operation you want to execute: ")
  num2 = int(input("Enter next number: "))
  calc = operator[op]
  ans = calc(num1,num2)
  print(f"= {ans}")
  checker = input ("Enter y if you want to try it again else press n: ")
  if (checker == 'n'):
    check_end +=1
  elif (checker == 'y'):
    num1 = ans
