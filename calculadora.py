def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def calculator():
   # Solicita dois números ao usuário
   num1 = int(input("Digite o primeiro número: "))
   num2 = int(input("Digite o segundo número: "))

   # Solicita ao usuário qual operação deseja realizar
   print("Qual operação deseja fazer: ")
   print("+ adição")
   print("- subtração")
   print("* multiplicação")
   print("/ divisão")

   # Lê a escolha do usuário
   choice = input("Escolheu (+/-/*//): ")

   if choice == '+':
      print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '-':
      print(num1,"-",num2,"=", subtract(num1,num2))

   elif choice == '*':
      print(num1,"*",num2,"=", multiply(num1,num2))

   elif choice == '/':
      print(num1,"/",num2,"=", divide(num1,num2))
   else:
      print("Operação invalida")


calculator()