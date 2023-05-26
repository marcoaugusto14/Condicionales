#Escriba un programa para verificar si un número es divisible o no por 5 y 11.

n=int(input("Ingrese un nùmero "))

if n % 5 ==0 and n % 11 ==0:
  print("El nùmero",n,"es divisible por 5 y 11")
else:
  print("El nùmero",n,"no es divisible por 5 y 11")