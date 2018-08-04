# now we have to solve the problem of finding the nth fib number by memoization menthod, i.e. 
# by following the top down approach, what we need to do, is to store the intermediate values calculated
# and return the answer when asked for..
def fib(n,fib_mem):
    
    if(fib_mem[n] == -1):
        if(n <=1):
            fib_mem[n] = n
        else:
            fib_mem[n] = fib(n-1,fib_mem) + fib(n-2,fib_mem)    
    return fib_mem[n]
fib_mem = [-1]*(20)
print(fib(5,fib_mem))
print(fib_mem)