#fuction count_a has the variable word
def count_a(word):
    #the original value of c is 0
    c = 0
    #if there is a letter a in the word in the variable word, the value of c will increase by 1
    for char in word:
        if char == 'a' or char == 'A':
            c += 1
# if c = 1, it will print letter A at the end
    if c == 1:
        print("This word has {0} letter A".format(c))
        #if c < 1 or c > 1, it will print As
    else: 
        print("This word has {0} letter As".format(c))
    
print (count_a("banana"))


