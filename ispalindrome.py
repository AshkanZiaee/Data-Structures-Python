

def palindrome(s):
    for i in range (len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


def re_palindrome(s):
    if len(s) < 2:
        if s[0] == s[-1]:
            return True
        else:
            return False
    else:
        return re_palindrome(s[1:-1])


s = "racecar"

print(re_palindrome(s))
print(palindrome(s))
