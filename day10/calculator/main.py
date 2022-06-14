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
while (check_end == 0):
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  operator = input("""Enter the operation you want to carry out: 
                   Addition : +
                   Subtraction: -
                   Multiplication: *
                   Division: /
                   : """)
  if (operator == '+'):
    print(add(num1,num2))
  elif (operator  == '-'):
    print(subtract(num1,num2))
  elif (operator == '*'):
    print(multiply(num1,num2))
  elif (operator == '/'):
    print (divide(num1,num2))
  else:
    print("Invalid input")
  checker = input ("Enter y if you want to try it again else press n")
  if (checker == 'n'):
    check_end +=1
