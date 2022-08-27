
number=1

number = int(input("Enter a number:"))

fact = 1

if number<0:
    print("Fctorial does not exist")
elif number==0:
    print("Factorial of 0 = 1")  
else:
    for i in range (1,number+1):
      fact = fact*i
    
print("Factorial of " ,number ,"is" ,fact,)