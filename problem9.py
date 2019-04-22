

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2


def get_triplets(max):
    for a in range(1, max-1):
        for b in range(1, max-2):
            c = max - (a + b)
            if c > 0:
                yield a, b, c


def main():
    for triplet in get_triplets(1000):
        if is_pythagorean_triplet(*triplet):
            print(f'I found it! Solution is {triplet}')
            break


if __name__ == '__main__':
    main()
