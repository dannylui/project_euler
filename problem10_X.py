from problem5_X import is_prime

prime_numbers = []
limit = 2000000
i = 2

while i < limit:
    if is_prime(i):
        prime_numbers.append(i)
    i += 1

print(sum(prime_numbers))