#Function is_palyndorm has variable word
def is_palindrome(word):
    #variable word is substituded for c
    c = word
    #b is the reverse order of letters in c
    b = c[::-1]
    #if the reverse order is equal to the normal order, it prints palindo
    if b == c:
        print("palindrome ")
    else:
        print("not palindrome ")
    
    
print (is_palindrome("racecar"))
   

