# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t = int(input())
results = []
for _ in range(t):
    a, b = input().split()
    type_a = a[-1]
    type_b = b[-1]
    
    if type_a != type_b:
        if type_a == 'S':
            results.append('<')
        elif type_a == 'M' and type_b == 'S':
            results.append('>')
        elif type_a == 'M' and type_b == 'L':
            results.append('<')
        elif type_a == 'L':
            results.append('>')
    else:
        if type_a == 'M':
            results.append('=')
        elif type_a == 'S':
            if len(a) == len(b):
                results.append('=')
            elif len(a) < len(b):
                results.append('>')
            else:
                results.append('<')
        elif type_a == 'L':
            if len(a) == len(b):
                results.append('=')
            elif len(a) < len(b):
                results.append('<')
            else:
                results.append('>')
print("\n".join(results))