def is_palindrome(str1, str2):
    if str1==str2:
        return True
    return False

def max_palindrome(start, end):
    palidromes = []
    for i in reversed(range(min,max)):
        for j in reversed(range(min,i)):
            product = i * j
            rev_product = str(product)[::-1]
            if is_palindrome(str(product),rev_product):
                 palidromes.append(product)
    return sorted(palidromes)[-1]

min = 100
max = 1000

print(max_palindrome(min,max))
