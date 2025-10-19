def fib(n):      #creating the function
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)          #base case

# print Fibonacci numbers till 10 digits
for i in range(10):
    print(fib(i), end=" ")
