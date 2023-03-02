print("введите секретны ключ")
d, m = map(int, input().split())
a = int(input())
while a != 0:
    print(a ** d % m)
    a = int(input())