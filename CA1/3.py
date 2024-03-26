def B_order(n, li, solution):
    if n <= 0:
        solution[0] += 1
        return

    for i in li:
        if i % n == 0 or n % i == 0:
            B_order(n - 1, list(filter(lambda x: x != i, li)), solution)
            continue

n = int(input())

solution = [0]

B_order(n, list(range(1, n + 1)), solution)

print(solution[0])