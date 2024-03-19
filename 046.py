# Lambda Function

# def mul(x,y):
#     return(x*y)

mul = lambda x,y: x*y
cube = lambda x: x**3

print(mul(1,2))
print(cube(2))

# Passing function as an Argument
def cal(fx,value):
    return(fx(value)+ 12)

print(cal(lambda x:x**3, 2))