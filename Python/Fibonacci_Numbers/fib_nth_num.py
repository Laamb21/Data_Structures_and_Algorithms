#Function to generate Nth Fibonacci number
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)
    
#Prompt user for nth Fobonacci number
nth_num = int(input("Enter desired Nth Fibonacci number: "))

#Print Nth Fibonacci number
print(F(nth_num))