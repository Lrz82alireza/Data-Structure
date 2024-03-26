n = input()

numbers_list = [int(digit) for digit in n]

first, max = 0, 0

flag = False


for i in range(1, len(numbers_list), 1):
    if numbers_list[i - 1] == numbers_list[i]:
        if flag:
            max = (i - first) if (i - first) > max else max
            first = temp
        else:
            flag = True

        temp = i
max = (len(numbers_list) - first) if (len(numbers_list) - first) > max else max

# print(first)
print(max)
            
