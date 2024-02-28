from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# Use Counter to count the occurrences of each number
counter = Counter(numbers)

# Initialize the answer and max_count
ans = 0
max_count = 0

# Iterate over the items in the Counter
for key, value in counter.items():
    if value > max_count:
        max_count = value
        ans = key

print(ans)
