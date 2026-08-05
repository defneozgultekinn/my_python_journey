# WHY USE return?
# Without return: the function does something (like printing),
# but the result is lost - you can't use it again later.
# With return: the function sends the result back to you,
# so you can store it in a variable and reuse it.
# Example without return
def add_no_return(a, b):
    print(a + b)   # just prints, doesn't give the value back
add_no_return(3, 4)   # prints 7, but nothing is stored

# Example with return
def add(a, b):
    return a + b   # sends the result back

result = add(3, 4)        # result = 7
result2 = add(result, 10) # result2 = 17, we reused "result"
print(result2)

def cube(num):
    return num*num*num
result= cube(3)
print(result)