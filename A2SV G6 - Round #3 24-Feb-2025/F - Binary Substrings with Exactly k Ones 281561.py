# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

def count_substrings_with_k_ones(k, s):
    positions = []
    for i, char in enumerate(s):
        if char == '1':
            positions.append(i)
    if k == 0:
        zero_count = 0
        result = 0
        for char in s:
            if char == '0':
                zero_count += 1
            else:
                result += zero_count * (zero_count + 1) // 2
                zero_count = 0
        result += zero_count * (zero_count + 1) // 2 
        return result
    result = 0
    for i in range(len(positions) - k + 1):
        start = positions[i]
        end = positions[i + k - 1]
        start_left = positions[i - 1] + 1 if i > 0 else 0
        end_right = positions[i + k] - 1 if i + k < len(positions) else len(s) - 1
        left_count = start - start_left + 1
        right_count = end_right - end + 1
        result += left_count * right_count

    return result
k = int(input())
s = input().strip()
print(count_substrings_with_k_ones(k, s))