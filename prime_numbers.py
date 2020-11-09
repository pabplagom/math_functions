import time

# Prime: calculate the prime numbers within the first n numbers iterating from 3 to n
# Input: last number
# Output: None

def prime(n):
    start_time = time.time()
    print("Calculating the first %s prime numbers" %n)  
    for prime in range (3,n):
        flag = 0
        for i in range (2,prime):
            if prime % i ==0:
                flag = 1
                break
        if flag ==0:
            print(prime, end=", ")
    print("\n Execution time: %s s" %(time.time()-start_time))

# Primeimproved2: calculate the prime numbers within the first n using and saving the prime numbers found during the process
# Input: last number
# Output: array of prime numbers

def primeimproved2(n):
    start_time = time.time()
    print("Calculating the first %s prime numbers" %n)    
    primedata = [2]   
    for prime in range(3,n):
        flag = 0
        i = 0
        while i < len(primedata):
            if prime % primedata[i] ==0:
                flag = 1
                break
            i = i + 1
        if flag == 0:
            primedata += [prime]
            print(prime, end=", ")
    print("\n Execution time: %s s" %(time.time()-start_time))
    return primedata
 
# Primeimproved2: calculate the prime numbers within the first n using and saving the prime numbers found during the process.
# it also discards values less than half of the evaluated number
# Input: last number
# Output: array of prime numbers
    
def primeimproved(n):
    start_time = time.time()
    print("Calculating the first %s prime numbers" %n)   
    primedata = [2]   
    for prime in range(3,n):
        flag = 0
        i = 0
        while i < len(primedata) and primedata[i] <= prime*2:
            if prime % primedata[i] ==0:
                flag = 1
                break
            i = i + 1
        if flag == 0:
            primedata += [prime]
            print(prime, end=", ")
    print("\n Execution time: %s s" %(time.time()-start_time))
    return primedata

#factorialdecomposition: find the descomposition of a given number n
# Input: number to be decomposed
# Output: factors

def factorialdecomposition(n):
    start_time = time.time()
    print("Calculating the factorial decompositon of %s: " %n, end="")
    factorial = []
    i = 2
    while i <= n:
        if n % i ==0:
            factorial += [i]
            n = n / i
        else:
            i = i + 1
    print(factorial)
    print("\n Execution time: %s s" %(time.time()-start_time))
    return factorial
