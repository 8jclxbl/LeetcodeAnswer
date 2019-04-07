def findJudge(N, trust):
    nom = [0 for i in range(N)]
    tru = [0 for i in range(N)]
    for i in trust:
        nom[i[0] - 1] += 1
        tru[i[1] - 1] += 1
    judge = -1
    for i in range(N):
        if nom[i] == 0 and judge == -1 and tru[i] == N-1:
            judge = i + 1
            break
    return judge