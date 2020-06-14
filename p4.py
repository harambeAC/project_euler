max= 0 

def ispalindrome(n):
    n = str(n)
    for i in range(int(len(n)/2)):
        if(n[i] != n[len(n) - 1 -i]):
            return False
    return True

for i in range(1000):
    for j in range(1000):
        if(i*j > max and ispalindrome(i*j)):
            max = i*j

print(max)
