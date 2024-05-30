
def count_mistakes(cities, i, max_num, last_LEFT = None, last_RIGHT = None):
    mistakes = 0
    cities[i].append(i)
    # print()
    # print(i, last_LEFT, last_RIGHT, cities[i])
    # left
    if cities[i][1] != -1: 
        l_index = cities[i][1]
        l_value = cities[l_index]

        if cities[i][0] < l_value[0]:
            # print("manam l_1", i)
            mistakes += 1
        if last_RIGHT != None and l_value[0] < last_RIGHT:
            # print("manam l_2", i)
            mistakes += 1
        if len(l_value) == 3:
            mistakes += count_mistakes(cities, l_index, max_num, cities[i][0], last_RIGHT)
            # print("biroon", i)

    # right
    if cities[i][2] != -1: 
        r_index = cities[i][2]
        r_value = cities[r_index]

        if cities[i][0] > r_value[0]:
            # print("manam r_1", i)
            mistakes += 1
        if last_LEFT != None and r_value[0] > last_LEFT:
            # print("manam r_2", i)
            mistakes += 1
        if len(r_value) == 3:
            mistakes += count_mistakes(cities, r_index, max_num, last_LEFT, cities[i][0])
            # print("biroon", i)

    if i < max_num and len(cities[i + 1]) == 3 and last_LEFT == None and last_RIGHT == None:
        mistakes += count_mistakes(cities, i + 1, max_num)

    return mistakes

n = int(input())

cities = {}

for i in range(n):
    city = [int(x) for x in input().split()]
    cities[i + 1] = city

count = count_mistakes(cities, 1, n)

print(count)