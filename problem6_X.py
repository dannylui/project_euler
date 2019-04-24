start = 1
end = 100

sum_of_squares = [num**2 for num in range(start,end+1)]
square_of_sums = [num for num in range(start,end+1)]


print(sum(sum_of_squares))
print(sum(square_of_sums)**2)

diff = sum(square_of_sums)**2 - sum(sum_of_squares)
print(diff)