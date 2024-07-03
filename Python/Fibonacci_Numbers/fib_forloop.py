#Initalize 0 and 1 for Fibonacci numbers
x = 0
y = 1

#Get number of iterations from user
size = input("Enter number of iterations: ")

#Print first two numbers
print(x)
print(y)

#Generate Fibonacci sequence with n iterations
for fibo in range(int(size)):
    newFibo = y + x 
    print(newFibo)  
    x = y 
    y = newFibo
