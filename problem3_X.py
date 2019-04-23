from datetime import datetime
import math


def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i == 0:
            return False
    return True


def get_factors2(num):
    factors = []
    if num % 2 == 0:
        factors.append(2)
        factors.append(int(num / 2))

    for i in range(3,int(math.sqrt(num))+1,2):
        # print(i)
        if num % i == 0:
            factors.append(i)
            factors.append(int(num/i))
    for i in sorted(factors, reverse=True):
        if is_prime(i):
            return i
    return 1


start_time = datetime.now()
# number = 13195
number = 600851475143
print(get_factors2(number))
print(f'Done in {(datetime.now() - start_time).total_seconds()}')
