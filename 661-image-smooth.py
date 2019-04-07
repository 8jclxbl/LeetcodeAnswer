def imageSmoother(M):
    r = len(M)
    c = len(M[0])

    delta = [-1,0,1]

    res = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            count = 9
            sum_ = 0
            for k in [i + t for t in delta]:
                if k < 0 or k > r-1:
                    count -= 3
                    continue
                for l in [j + t for t in delta]:
                    if l < 0 or l > c-1:
                        count -= 1
                    else:
                        sum_ += M[k][l]
            res[i][j] = sum_//count
    return res

M = [[1,1,1],[1,0,1],[1,1,1]]
print(imageSmoother(M))
