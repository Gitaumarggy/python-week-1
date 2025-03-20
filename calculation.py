calculation= []
for i in range (1):
    operator=input("enter an operator (+,-,*,/)")
num1=int(input ("enter the first integer:"))
num2=int(input ("enter the second integer:"))
if operator =='+':
    print (f"{num1}+{num2}={num1+num2}")
elif operator =='-':
     print (f"{num1}-{num2}={num1-num2}")
elif operator =='*':
     print (f"{num1}*{num2}={num1*num2}")
elif operator =='/':
    if num2 ==0:
        print ("cannot be divided by zero")
    else:
        print (f"{num1}/{num2}={num1/num2}")
else :
    print ("invalid operator")
