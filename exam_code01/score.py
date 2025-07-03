score = list(map(int, input('점수입력:').split()))
#print(score)

total = 0 #변수선언
for i in range(len(score)):
    total += score[i]

print(f'총점 : {total}')
print(f'평균 : {total / len(score):.2f}')
