# 5 12 23 34 45 54 56 234 345 3432
# 23 34 234 5 12 345 3432 45 54 56
numbers = [int(param) for param in input().split()]

# selection sort - (1)
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(' '.join(str(num) for num in numbers))

# selection sort - (2)
for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        value = numbers[j]
        if value > numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# selection sort - (3)
def selection_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)