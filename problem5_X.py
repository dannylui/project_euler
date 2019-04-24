import math


def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


def get_prime_factors(num):
    if is_prime(num):
        return [num]

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0 and is_prime(i):
            j = int(num/i)
            return [i] + get_prime_factors(j)


def common_factors(start, end):
    product = end
    for i in reversed(range(start, end)):
        factors = get_prime_factors(i)
        temp = 1
        temp_product = product
        for j in factors:
            if temp_product % j == 0:
                temp_product = int(temp_product/j)
            else:
                temp *= j
        product *= temp

    return product


def main():
    print(common_factors(1, 20))


if __name__ == "__main__":
    main()
