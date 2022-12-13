def sum_to(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

def sum_tow(n):
    total = 0
    i = 0
    x = range(n+1)
    while i <= n:
        total += i
    return total


print(sum_tow(87))