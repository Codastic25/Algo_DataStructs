def is_palindrome(s):
    s = s.lower() # to make sure that there is no problem with sensitive case
    for i in range(len(s)//2):
        if s[i] != s[-i-1] :
            return False
    return True
