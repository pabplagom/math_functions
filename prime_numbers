import time

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
    
def factorialdescomposition(n):
    start_time = time.time()
    print("Calculating the factorial descompositon of %s: " %n, end="")
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
