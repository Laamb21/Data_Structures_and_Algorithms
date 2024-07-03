x = 0
y = 1

size = input("Enter number of iterations: ")

print(x)
print(y)
for fibo in range(int(size)):
    newFibo = y + x 
    print(newFibo)  
    x = y 
    y = newFibo
