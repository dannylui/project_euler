from datetime import datetime
from tqdm import tqdm, trange
import  math

# number = 600851475143

def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3,int(math.sqrt(num)),2):
        if num % i == 0:
            return False
    return True


def get_factors(num):
    # for i in tqdm(reversed(range(1, int(num/2+1), 2)), ncols=100, ascii=True):
    half=int(num/2)
    if half % 2 == 0:
        half += 1
    for i in trange(2, half, 2):
        j = half - i
        # print(j)
        if num % j == 0:
            if is_prime(j):
                return j
    return 1

def get_factors2(num):
    for i in reversed(range(3,int(math.sqrt(num))+1,2)):
        print(i)
        if num % i == 0:
            if is_prime(i):
                return i
    return 1

number = 16

# def get_factors(num):
#     factors = []
#     for i in range(2,num+1):
#         if num % i == 0:
#             factors.append(i)
#
#     return factors

# print(get_factors(13195))

print(f'I\'m starting at {datetime.now()}')
print(get_factors2(number))
# print(get_factors(13195))
# print(get_factors(105))
# print(get_factors(600851475))
print(f'I\'m done at {datetime.now()}')

# def is_prime_2(num):
#     return len(get_factors(num)) == 1

# for i in range(1,50):
# #     # print(str(i) + ":" + str(is_prime(i)))
# #     # print(str(i) + ":" + str(is_prime_2(i)))
#     print(str(i) + ":" + str(get_factors(i)))


# factors = filter(is_prime, get_factors(number))

# print(list(factors))


