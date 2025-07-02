score = list(map(int, input('').split()))

if any(s < 0 or s > 100 for s in score):
    print('잘못된 점수')
else : 
    avg = sum(score) / len(score)
    if avg >= 80:
        print('합격!')
    else:
        print('불합격!')
