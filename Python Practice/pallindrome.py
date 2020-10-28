def isPalindrome(S):
    isPalindrome = False
    for i in range(0,len(S)):
        if S[i] == S[len(S)-1-i]:
            isPalindrome = True
        else:
            isPalindrome = False
    return isPalindrome
x = isPalindrome("foolproof")
print(x)


or

def isPalindrome(S):
    for i in range(0,len(S)):
        if S[i] == S[len(S)-1-i]:
            y = True
        else:
            y = False

    if y == True:
        return True
    else:
        return False


print(isPalindrome("foolproof"))