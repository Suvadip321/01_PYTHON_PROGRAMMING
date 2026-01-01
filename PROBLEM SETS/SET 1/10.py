# def isPalindrome(n):
#   n = str(n)
#   return n == n[::-1]

def isPalindrome(n):
    temp, rev = n, 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return n == rev


n = int(input("enter a positive integer number: "))
print(isPalindrome(n))
