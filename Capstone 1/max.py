

numbers = [22, 46, 78, 15, 98, 101]
max_num = 0
for i in numbers:
    if i > max_num:
        max_num = i
print(numbers.index(max_num))