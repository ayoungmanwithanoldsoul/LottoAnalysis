from itertools import combinations

# Given list
numbers = [19, 15, 31, 4, 5, 25, 18, 22, 12, 16]

# Generate all combinations of 6 elements
all_combinations = list(combinations(numbers, 6))

# Display the first 10 combinations as an example
for i in range(210):
    print(f"{''}. {', '.join(map(str, all_combinations[i]))}")

# Total number of combinations
total_combinations = len(all_combinations)
print(f"\nTotal number of combinations: {total_combinations}")
