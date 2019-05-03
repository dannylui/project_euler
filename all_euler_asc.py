import logging
from datetime import datetime
import math
from functools import reduce


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)+1), 2):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    num_as_str = str(num)
    return num_as_str == num_as_str[::-1]


class Prime:
    init_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                   103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    known_primes = set(init_primes)

    @classmethod
    def is_prime(cls, number):
        # 0, 1 and negative numbers are not prime
        if number < 2:
            return False

        # check if we already know its a prime
        if number in cls.known_primes:
            return True

        # check if its divisible by the known primes
        for i in cls.known_primes:
            if number % i == 0:
                return False

        # check divisibility from last known prime to the square root of the number
        # also only check odd numbers
        for j in range(max(cls.init_primes)+2, int(math.sqrt(number))+1, 2):
            if number % j == 0:
                return False

        # found no factor, so it must be prime
        cls.known_primes.add(number)
        return True

    @staticmethod
    def gen_primes(limit):
        primes_found = set()
        candidate = 2
        while candidate <= limit:
            primes_found.add(candidate)
            yield candidate

            candidate += 1
            candidate_sqrt = int(math.sqrt(candidate))
            prime = False

            while not prime:
                prime = True
                for prime in sorted(primes_found):
                    if prime > candidate_sqrt:
                        break
                    if candidate % prime == 0:
                        prime = False
                        candidate += 1
                        candidate_sqrt = int(math.sqrt(candidate))
                        break

    @staticmethod
    def primes_sieve2(limit):
        """ from https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python """
        a = [True] * (limit+1)  # Initialize the primality list
        a[0] = a[1] = False

        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i*i, limit+1, i):  # Mark factors non-prime
                    a[n] = False

    @staticmethod
    def is_prime_2(num):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in Prime.gen_primes(int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def is_prime_3(num):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in Prime.primes_sieve2(int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True


def euler_1(limit=10, divisors=(3, 5)):
    multiples = []
    for i in range(1, limit):
        is_multiple = False
        for divisor in divisors:
            if i % divisor == 0:
                is_multiple = True
        if is_multiple:
            multiples.append(i)
    # logging.debug(f'Multiples found {multiples}')
    return sum(multiples)


def euler_2(limit=100):
    fibs = [1, 2]
    while fibs[-1] <= limit:
        fibs.append(fibs[-1] + fibs[-2])

    # logging.debug(f'Fibonacci seq up to {limit} is {fibs}')
    return sum(list(filter(lambda x: x % 2 == 0, fibs)))


def euler_3(limit=13195):
    factors = []
    for i in range(2, int(math.sqrt(limit))):
        if limit % i == 0:
            factors.append(i)
    logging.debug(f'Factors: {factors}')
    for j in reversed(factors):
        if is_prime(j):
            return j


def euler_3b(limit=13195):
    for i in reversed(range(3, int(math.sqrt(limit)), 2)):
        if limit % i == 0 and is_prime(i):
            return i
    if limit % 2 == 0:
        return 2


def euler_4(digits=2):
    limit = int('9'*digits)

    for i in reversed(range(1, limit+1)):
        for j in reversed(range(1, limit+1)):
            if is_palindrome(i*j):
                return i, j


def euler_5(a=1, b=10):
    smallest_multiple = b
    found = False

    while not found:
        found = True
        for i in range(a, b + 1):
            if smallest_multiple % i != 0:
                found = False
                smallest_multiple += 1
                break
        if found:
            break
    return smallest_multiple


def euler_6(limit=10):
    source = range(1, limit+1)
    square_of_sums = sum(source)**2
    sum_of_squares = sum(map(lambda x: x**2, source))
    return square_of_sums - sum_of_squares


def euler_7(prime=6):
    primes = [2, 3, 5, 7, 11]
    candidate = max(primes)
    while len(primes) < prime:
        candidate += 1
        if is_prime(candidate):
            primes.append(candidate)
    return primes[-1]


class Euler196:
    def __init__(self, n):
        self._n = n
        self.last_info_time = self.start_time = datetime.now()

        self._known_primes = set()
        self._known_non_primes = set()
        self._n_primes = set()
        self._rows = {}

        for i in range(n-2, n+3):
            self.set_row(i, self.get_row_numbers(i))

        # TODO handle edge cases n = 1 or n = 2?

    def set_row(self, row, numbers):
        self._rows[str(row)] = numbers

    def print_rows(self):
        for row, numbers in self._rows.items():
            print(f'{row}: {numbers}')

    def find_number(self, number):
        for row, numbers in self._rows.items():
            if number in numbers:
                return int(row), numbers.index(number)

    def get_cell(self, row, col):
        row = str(row)
        if row in self._rows:
            if 0 <= col < len(self._rows[row]):
                return self._rows[row][col]
        return None

    def is_prime(self, number):
        if number in self._known_primes:
            return True
        if number in self._known_non_primes:
            return False
        if is_prime(number):
            self._known_primes.add(number)
            return True
        else:
            self._known_non_primes.add(number)
            return False

    def print_info(self, index, interval_in_secs=300):
        now = datetime.now()
        if (now - self.last_info_time).seconds > interval_in_secs:
            progress = (100.0 * index) / self._n
            time_spent = (now - self.start_time).seconds
            est_total_time = (time_spent * 100.0) / progress
            est_time_remaining = est_total_time - time_spent
            logging.info(f'{progress:.2f}% complete...  '
                         f'{len(self._known_primes)} primes discovered, '
                         f'{len(self._n_primes)} are elements of some prime triplet.  '
                         f'[estimated (mins): {est_total_time / 60:.0f} total | '
                         f'{est_time_remaining / 60:.0f} remaining]')
            self.last_info_time = now

    def solve(self, info_interval_in_secs=60):
        # using lists: completed in 1.784949
        # using sets: completed in 0.25997 seconds
        # checking neighbors only once: completed in 0.246003 seconds
        logging.info(f'Starting calculations, printing info every {info_interval_in_secs} secs...')
        for index, number in enumerate(self._rows[str(self._n)]):
            self.print_info(index, info_interval_in_secs)
            is_triplet = False
            if self.is_prime(number):
                neighbors = self.get_neighbors(self._n, index)
                prime_neighbors = []
                for neighbor in neighbors:
                    if self.is_prime(neighbor):
                        prime_neighbors.append(neighbor)
                        if len(prime_neighbors) > 1:
                            is_triplet = True
                            break
                if not is_triplet:
                    for prime_neighbor in prime_neighbors:
                        for second_neighbor in self.get_neighbors(*self.find_number(prime_neighbor), number):
                            if self.is_prime(second_neighbor):
                                is_triplet = True
                                break
                if is_triplet:
                    self._n_primes.add(number)
        return sum(self._n_primes)

    @staticmethod
    def get_row_start(row):
        return int(row * (row - 1) / 2 + 1)

    def get_row_numbers(self, row):
        start = self.get_row_start(row)
        numbers = []
        for i in range(row):
            numbers.append(start + i)
        return numbers

    def get_neighbors(self, row, col, exclude=-1):
        if self.get_cell(row, col):
            neighbors = []
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if not (i == row and j == col):
                        number = self.get_cell(i, j)
                        if number and number != exclude:
                            neighbors.append(number)
            return neighbors
        return []


def euler_196(a=5678027, b=7208785):
    return Euler196(a).solve() + Euler196(b).solve()


def run_problem(description, problem, arg):
    start_time = datetime.now()
    logging.info('Running: %s', description)
    if isinstance(arg, tuple):
        solution = problem(*arg)
    else:
        solution = problem(arg)
    logging.info(f'    solution: {solution}')
    logging.info('    completed in %s seconds', (datetime.now() - start_time).total_seconds())


def test_is_palidrome():
    assert is_palindrome(1)
    assert is_palindrome(121)
    assert not is_palindrome(123)
    assert is_palindrome(1221)
    assert is_palindrome(123456787654321)
    assert is_palindrome(12345677654321)
    assert not is_palindrome(12345677654312)


def test_prime_checker():
    for x in range(1000):  # initialize prime checker
        Prime.is_prime(x)

    assert not Prime.is_prime(0)
    assert not Prime.is_prime(-1)
    assert not Prime.is_prime(1)
    assert Prime.is_prime(2)
    assert Prime.is_prime(3)
    assert not Prime.is_prime(4)
    assert Prime.is_prime(5)
    assert not Prime.is_prime(6)
    assert Prime.is_prime(7)
    assert Prime.is_prime(11)
    assert not Prime.is_prime(123)
    assert not Prime.is_prime(21321)
    assert Prime.is_prime(29)
    assert Prime.is_prime(41)
    assert Prime.is_prime(851475143)
    assert not Prime.is_prime(4453452)
    assert Prime.is_prime(6857)
    assert not Prime.is_prime(25)
    assert not Prime.is_prime(35)


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(-1)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert is_prime(11)
    assert not is_prime(123)
    assert not is_prime(21321)
    assert is_prime(29)
    assert is_prime(41)
    assert is_prime(851475143)
    assert not is_prime(4453452)
    assert is_prime(6857)
    assert not is_prime(25)


def test_euler_196():
    e = Euler196(3)
    assert e.get_cell(1, 0) == 1
    assert e.get_cell(2, 1) == 3
    assert e.get_cell(5, 4) == 15
    assert e.get_cell(0, 0) is None
    assert e.get_cell(1, 1) is None
    assert e.get_cell(4, 4) is None
    assert e.get_neighbors(4, 1) == [4, 5, 6, 7, 9, 11, 12, 13]
    assert e.get_neighbors(4, 0) == [4, 5, 8, 11, 12]
    assert e.get_neighbors(1, 0) == [2, 3]
    assert e.get_neighbors(1, 1) == []
    assert e.get_neighbors(3, 2) == [3, 5, 8, 9, 10]
    assert e.get_neighbors(5, 4) == [10, 14]
    assert e.get_neighbors(2, 1) == [1, 2, 4, 5, 6]
    assert e.get_neighbors(4, 1, 6) == [4, 5, 7, 9, 11, 12, 13]
    assert e.find_number(1) == (1, 0)
    assert e.find_number(0) is None
    assert e.find_number(4) == (3, 0)
    assert e.find_number(6) == (3, 2)
    assert e.find_number(14) == (5, 3)

    assert Euler196(8).solve() == 60
    assert Euler196(9).solve() == 37


def loop_is_prime(is_prime_func, start, loop=100):
    primes = []
    num = start
    for i in range(loop):
        num += 1
        if is_prime_func(num):
            primes.append(num)
    return len(primes)


def test_is_prime_perf():
    loop = 100
    number = 600851475143
    run_problem('test is_prime', loop_is_prime, (is_prime, number, loop))
    run_problem('test Prime.is_prime', loop_is_prime, (Prime.is_prime, number, loop))
    run_problem('test Prime.is_prime_2', loop_is_prime, (Prime.is_prime_2, number, loop))
    run_problem('test Prime.is_prime_3', loop_is_prime, (Prime.is_prime_3, number, loop))


def get_factors(num):
    for i in Prime.gen_primes(int(math.sqrt(num))+1):
        if num % i == 0:
            j = int(num/i)
            return [i] + ([j] if is_prime(j) else get_factors(j))
    return [num]


def euler_5b(start, end):
    all_factors = get_factors(end)
    for i in reversed(range(start, end)):
        # print(f'all: {all_factors}, i: {i}')
        all_factors_copy = all_factors[:]
        factors = get_factors(i)
        for f in get_factors(i):
            if f in all_factors_copy:
                all_factors_copy.remove(f)
                factors.remove(f)
        all_factors.extend(factors)
        # print(f'    new: {factors}')
    return reduce((lambda x, y: x * y), all_factors)

def euler_7b(limit):
    for i, p in enumerate(Prime.gen_primes(104743)):
        if i == limit-1:
            return p

def euler_7c(limit):
    for i, p in enumerate(Prime.primes_sieve2(104743)):
        if i == limit-1:
            return p

def main():
    # run_problem('Euler 1', euler_1, 1000)
    # run_problem('Euler 2', euler_2, 4000000)
    # run_problem('Euler 3', euler_3, 600851475143)
    # run_problem('Euler 3b', euler_3b, 600851475143)
    # run_problem('Euler 4', euler_4, 3)
    # run_problem('Euler 5', euler_5, (1, 20))  # takes 95s
    # run_problem('Euler 5b', euler_5b, (1, 20))  # instant finish
    # run_problem('Euler 6', euler_6, 100)
    run_problem('Euler 7', euler_7, 10001)
    run_problem('Euler 7b', euler_7b, 10001)
    run_problem('Euler 7c', euler_7c, 10001)
    # run_problem('Euler 196', euler_196, (5678027, 7208785))  # takes 2 days and 8.5 hours
    # run_problem('Euler 196', euler_196, (3, 10000))  # takes 1.7s
    # run_problem('Euler 196', euler_196, (3, 1000000))  # takes 30 mins

    # a = Prime.primes_sieve2(104743)
    # b = Prime.gen_primes(104743)
    # x = next(a)
    # y = next(b)
    # while x == y:
    #     print(f'{x} is {y}?')
    #     x = next(a)
    #     y = next(b)
    # print(f'{x} is not {y}?')




if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
