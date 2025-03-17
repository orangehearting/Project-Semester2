import random

x=random.randint(10,20)

y=0
while y!=x:


   y=int(input("the number you guess is(from 10 to 20):")) 
   if y>x:
       print("too big.")
   elif y<x:
       print("too small")
   else:
       break
print("you gess the right number.")

