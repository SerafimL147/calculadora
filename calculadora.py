def numerod(x, y):
   return x + y

def subtracao(x, y):
   return x - y

def multiplic(x, y):
   return x * y

def divisao(x, y):
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
   choice = input("Escolha a operação (+/-/*//): ")

   if choice == '+':
      print(num1,"+",num2,"=", numerod(num1,num2))

   elif choice == '-':
      print(num1,"-",num2,"=", subtracao(num1,num2))

   elif choice == '*':
      print(num1,"*",num2,"=", multiplic(num1,num2))

   elif choice == '/':
      print(num1,"/",num2,"=", divisao(num1,num2))
   else:
      print("Operação invalida")


calculator()