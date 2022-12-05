#Prompts the user to enter a number
print("type a number")
#variable b is equal to the input from the user
b = input()
#c coverts the string b to be an integer
c = int(b)

def ran(d):
    #e = the ramge in the variable put im the functio 
    e = range(d)
    #p = the range of e + the initial variablle 
    for n in e:
        p = sum(e) + d
        return(p)

print(ran(c))
