from datetime import datetime
import math


def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


def get_factors(num):
    factors = []
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            factors.extend([i, int(num/i)])
    if num % 2 == 0:
        factors.append([2, int(num/2)])
    return factors


def get_max_prime_factor(num):
    for p in reversed(sorted(get_factors(num))):
        if is_prime(p):
            return p


def get_max_prime_factor_faster(num):
    max_prime_factor = 1

    if num % 2 == 0:
        num_div_by_2 = int(num/2)
        if is_prime(num_div_by_2) and num_div_by_2 > max_prime_factor:
            max_prime_factor = num_div_by_2
        else:
            max_prime_factor = 2

    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            j = int(num/i)
            if is_prime(j) and j > max_prime_factor:
                max_prime_factor = j
            if is_prime(i) and i > max_prime_factor:
                max_prime_factor = i

    return max_prime_factor


start_time = datetime.now()
print(get_max_prime_factor(13195))
print(get_max_prime_factor(600851475143))
print(f'Done in {(datetime.now()-start_time).total_seconds()}')

start_time = datetime.now()
print(get_max_prime_factor_faster(13195))
print(get_max_prime_factor_faster(600851475143))
print(f'Done in {(datetime.now()-start_time).total_seconds()}')


x = [1,3,4]
sorted