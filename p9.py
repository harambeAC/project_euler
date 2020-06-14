for i in range(1,1000):
    for j in range(1,i):
        k = 1000-i-j
        if(i**2 == k**2 + j**2):
            print(str(i) + "  " + str(j) + "  " + str(k))