# ok lets think how we can do this, first the method is tabulation method, it means that we have
# to solve it by bottom to up approach, so i need to store first fib number then second and so on, 
# for that I should iterate till the nth number and store all the required intermediate values in the table

def fib(n):
    # lets initialize the table now
    fib_table = [0]*(n+1)
    # and then give the initial value to the table
    fib_table[0] = 0
    fib_table[1] = 1
    # and now lets iterate till n, i.e. till we find the required fib number
    for i in range(2,n+1):
        # observe here that we are calculating the solution from already calculated values,i.e. already solved subproblems
        fib_table[i] = fib_table[i-1] + fib_table[i-2] 
     # and finally return the answer, which is the last element of the array
    return fib_table[n]
print(fib(2))  
