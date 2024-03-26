def sorted_seperate_odd_even(s):
    odd = [s[i] for i in range(len(s)) if i % 2 == 0]
    even = [s[i] for i in range(len(s)) if i % 2 != 0]
    return sorted(odd), sorted(even)

first = input()
second = input()

first_odd, first_even = sorted_seperate_odd_even(first)
second_odd, second_even = sorted_seperate_odd_even(second)

# print(first_odd, first_even)
# print(second_odd,second_even)

print("yes" if (first_odd == second_odd) and (first_even == second_even) else "no")