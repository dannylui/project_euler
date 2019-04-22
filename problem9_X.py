def pyth(a, b, c):
    return a**2 + b**2 == c**2

def find_trip(ran):
    for i in range(1,ran):
        for j in range(2,ran-1):
            if i+j<ran:
                c = ran-i-j
                if pyth(i,j,c):
                    return i,j,c


res=find_trip(1000)
print(res)
