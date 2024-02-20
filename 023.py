#Recursion in Python
# Defining something in terms of itself is recursion i.e fuction calling itself 
# factorial calculation
def factorial (num):
    if num==1 or num==0:
        return(1)
    else:
        return(num * factorial(num-1))
    
print(factorial(5))
# print(factorial(6))
# print(factorial(7))
# print(factorial(8))

# Fibonacii series calculation
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# fn = f(n-1) + f(n-2)
def fibo(n):
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    else:
        return(fibo(n-1) + fibo(n-2))
print(fibo(8))