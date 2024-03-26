def find_blocked_pairs(hashes, limit, rows):
    pairs = []

    for i in range(rows):

        temp = []
        flage_2 = False
        for hashe in hashes:
            if hashe[0] == i:
                flage_2 = True
                temp.append(hashe)
            elif flage_2:
                break

        if not temp:
            pairs.append(((i, -1), (i, limit)))
            continue
        for k in range(len(temp)):
            if k == 0:
                pairs.append(((i, -1), temp[k]))
            else:
                pairs.append((temp[k - 1], temp[k]))
        pairs.append((temp[-1], (i, limit)))

    return pairs

# def are_intersected(row_pair, col_pair):
#     if row_pair[0][1] < col_pair[0][1] < row_pair[1][1] and col_pair[0][0] < row_pair[0][0] < col_pair[1][0]:
#         return True 
#     return False

def find_most_dots(row_pairs, col_pairs):
    max = 0
    for row_pair in row_pairs:
        flage = False
        row_dots = abs(row_pair[0][1] - row_pair[1][1]) - 1
        for col_pair in col_pairs:
            sum_dots = row_dots + abs(col_pair[0][0] - col_pair[1][0]) - 2
            if max < sum_dots:
                if row_pair[0][1] < col_pair[0][1] < row_pair[1][1]:
                    flage = True
                    if col_pair[0][0] < row_pair[0][0] < col_pair[1][0]:
                        max = sum_dots
                elif flage:
                    break
    return max


row, column = input().split()

hashes = []
for i in range(int(row)):
    temp = input()
    for j in range(int(column)):
        if temp[j] == '#':
            hashes.append((i, j))

row_pairs = find_blocked_pairs(hashes, int(column), int(row))

transposed_hashes = [(j, i) for i, j in hashes]

col_pairs = find_blocked_pairs(sorted(transposed_hashes), int(row), int(column))
col_pairs = [((j, i), (z, k)) for ((i, j), (k, z)) in sorted(col_pairs)]

print(find_most_dots(row_pairs, col_pairs))

max = 0
dots_in_columns = []

