# -*- coding: utf-8 -*-
"""CodigosEVALUACION1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YevTUSVkKXO0Cf2QcG-voYonJ3drYOqF
"""

print ("Evaluación N°1 Programación y Redes Virtualizadas ")
print ("Andres, Angel, Francisco")

firstName = input("Cual es tu nombre? ")
lastName = input("Cual es tu apellido? ")
SeccionCode = input("Cual es tu seccion? ")
print (" Bienvenido " + firstName, lastName + "! Tu Seccion es "+ SeccionCode)

aclNum = int(input("Cual es el número IPV4 ACL? "))
if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL IPv4 estándar.")
elif aclNum >=100 and aclNum <= 199:
    print("Este es una ACL IPv4 extendida")

else:
    print("Esta ACL IPv4 no es extendida o estandar .")