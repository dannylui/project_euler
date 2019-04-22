import numpy as np

fibo=np.array([1,2])

limit=40

for step in range(limit):
    fibo = np.append(fibo,fibo[-1]+fibo[-2])

fibo_even = fibo[np.logical_and(fibo<4000000,fibo%2==0)]
# fibo_fil=fibo[fibo<4000000]
# fibo_even = fibo_fil[fibo_fil%2==0]

sum =sum(fibo_even)

# sum = 0

# for item in fibo_fil:
#     if item % 2 == 0:
#         sum += item


print(sum)