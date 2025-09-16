print("This is a calculator made by NIHAL M NAZEER")
print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
from divide import divi
from mult import multiply
from sub import subtr
from sum import addit
sel = int(input("Select operation (1-4): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if sel == 1:
    addit(n1,n2)
elif sel == 2:
    subtr(n1,n2)
elif sel == 3:
    multiply(n1,n2)
elif sel == 4:
    divi(n1,n2)
else:
    print("Invalid input")