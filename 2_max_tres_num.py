#Escriba un programa para encontrar el máximo entre tres números.

a=input("Ingrese el primer nùmero ")
b=input("Ingrese el segundo nùmero ")
c=input("Ingrese el tercer nùmero ")

if a>b and a>c:
   print("El nùmero mayor es ", a)
elif b>a and b>c:
  print("El nùmero mayor es ", b)
elif c>a and c>b:
  print("El nùmero mayor es ", c)
else:
  print("no hay ningun nùmero mayor")