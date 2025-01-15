class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        l=[(0,1),(0,-1),(1,0),(-1,0)]
        visit=[[False]*m for _ in range(n)]
        def can(x,y,k):
            return not visit[x][y] and 0<=x<n and 0<=y<m and board[x][y]==k
        def solve(x,y,t):
            for dx,dy in l:
                nx,ny=dx+x,dy+y
                if can(nx,ny,word[t]):
                    if t==len(word)-1:
                        return True
                    visit[nx][ny]=True
                    if solve(nx,ny,t+1):
                        return True
                    visit[nx][ny]=False
                return False
        for i in range(n):
            for j in range(m):
                if solve(i,j,0):
                    return True
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        l=[(0,1),(0,-1),(1,0),(-1,0)]
        visit=[[False]*m for _ in range(n)]
        def can(x,y,k):
            return 0<=x<n and 0<=y<m and board[x][y]==word[k] and not visit[x][y]
        def solve(x,y,t):
            if not can(x,y,t):
                return False
            if t==len(word)-1:
                return True
            visit[x][y]=True
            for dx,dy in l:
                nx,ny=dx+x,dy+y
                if solve(nx,ny,t+1):
                    return True
            visit[x][y]=False
            return False
        for i in range(n):
            for j in range(m):
                if solve(i,j,0):
                    return True
        return False