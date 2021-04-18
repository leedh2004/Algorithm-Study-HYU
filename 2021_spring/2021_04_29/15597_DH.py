from collections import defaultdict

A, B, C, D = input().split()
L = [(A, B), (A, C), (A, D), (B, C), (B, D), (C, D)]

countryToInt = defaultdict(int)
countryToInt[A] = 0
countryToInt[B] = 1
countryToInt[C] = 2
countryToInt[D] = 3

predict = [ [0.0] * 4 for _ in range(4) ]

for _ in range(6):
    a, b, w, d, l = input().split()
    a = countryToInt[a]
    b = countryToInt[b]
    w, d, l = float(w), float(d), float(l)
    predict[a][b] = (w, d, l)
    predict[b][a] = (l, d, w)

last_predict = defaultdict(int)

def make_results(cnt, results):
    global L, A, B, C, D, predict, countryToInt, last_predict 
    if cnt == len(L):
        dd = defaultdict(int)
        p = 1.0
        for a, b, result in results:
            ai, bi = countryToInt[a], countryToInt[b]
            if result == 'w':
                dd[a] += 3
                p *= predict[ai][bi][0]
            elif result == 'd':
                dd[a] += 1
                dd[b] += 1
                p *= predict[ai][bi][1]
            else:
                dd[b] += 3
                p *= predict[ai][bi][2]
        # 결과가 나왔는데, 동점자가 있는경우 처리해야 함
        if p > 0:
            parse_list = [(dd[A], A), (dd[B], B), (dd[C], C), (dd[D], D)]
            parse_list.sort(reverse=True)
            score = [ [] for _ in range(10) ]
            for s, c in parse_list:
                score[s].append(c)
            cnt = 0
            for i in range(9, -1, -1):
                num = len(score[i])
                if num > 0:
                    if cnt + num <= 2:
                        for c in score[i]:
                            last_predict[c] += p
                    else:
                        for c in score[i]:
                            last_predict[c] += p / num * ( 2 - cnt )
                    cnt += num
                if cnt >= 2:
                    break
        return
    a, b = L[cnt]
    make_results(cnt+1, results + [(a, b, 'w')])
    make_results(cnt+1, results + [(a, b, 'd')])
    make_results(cnt+1, results + [(a, b, 'l')])

make_results(0, [])
print(last_predict[A])
print(last_predict[B])
print(last_predict[C])
print(last_predict[D])