class Solution:
    def numRookCaptures(self, board):
        r = c = 8

        find = False
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'R':
                    rook = (i,j)
                    find = True
                    break
            if find: break
        count = 0 

        for i in range(rook[0]-1,-1,-1):
            if board[i][rook[1]] == 'B':break
            if board[i][rook[1]] == 'p':
                count += 1
                break
        for i in range(rook[0]+1,c):
            if board[i][rook[1]] == 'B':break
            if board[i][rook[1]] == 'p':
                count += 1
                break

        for i in range(rook[1]-1,-1,-1):
            if board[rook[0]][i] == 'B':break
            if board[rook[0]][i] == 'p':
                count += 1
                break
        for i in range(rook[1]+1,r):
            if board[rook[0]][i] == 'B':break
            if board[rook[0]][i] == 'p':
                count += 1
                break
        return count

if __name__ == "__main__":
    test = [[".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","R",".",".",".","p"],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]]


    s = Solution()
    print(s.numRookCaptures(test))
