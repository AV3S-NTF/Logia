from math import*

def ile(n, a):
    length = 1
    y = 0
    count = 0
    check = ''
    lengthcount = 0
    
    for i in range(0, n):
        length = length * 10
        
    length = length - 1
    
    for i in range(int((length + 1) / 10), length):
        check = str(i)
        lengthcount = len(check)
        for y in range(0, lengthcount):
            if (check[y] == str(a)):
                count = count + 1
                break
            y = y + 1
    print(count)
        
ile(3, 6)
