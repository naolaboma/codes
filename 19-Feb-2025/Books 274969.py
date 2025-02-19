# Problem: Books - https://codeforces.com/contest/279/problem/B

def max_books(n, t, books):
    start = 0
    current_time = 0
    max_books = 0
    for end in range(n):
        current_time += books[end]
        while current_time > t:
            current_time -= books[start]
            start += 1
        max_books = max(max_books, end - start + 1)
    return max_books
n, t = map(int, input().split())
books = list(map(int, input().split()))
print(max_books(n, t, books))