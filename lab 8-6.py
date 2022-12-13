#fucton factorial has variable num
def factorial(num):
    #b is the sum of all the range of num and c adds the value of num
    for x in range(num):
        b = sum(range(num))
        c = b + num

    print(c)
        
print(factorial(12))
