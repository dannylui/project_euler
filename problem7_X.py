from problem5_X import is_prime


# print(is_prime(5))
# print(is_prime(6))

prime_numbers = []
limit = 10001
i = 2

while len(prime_numbers) < limit:
    if is_prime(i):
        prime_numbers.append(i)
    i += 1

print(prime_numbers)
print(prime_numbers[-1])