#파이썬 2차원 리스트 만들기
a = [[0 for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        print(a[i][j], end=' ')
    print()
