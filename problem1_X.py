def is_multiple(a,n):
    return a%n==0

res=[]

for i in range(1,1000):
    if is_multiple(i,3) or is_multiple(i,5):
        res.append(i)

print(sum(res))