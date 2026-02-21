from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        queue = deque([])
        
        # add starting "O" coordinates at the boundary to the queue
        for i in range(m):
            if board[i][0] == "O":
                queue.append((i, 0))
                visited[i][0] = True
            if board[i][n-1] == "O":
                queue.append((i, n-1))
                visited[i][n-1] = True
        for i in range(n):
            if board[0][i] == "O":
                queue.append((0, i))
                visited[0][i] = True
            if board[m-1][i] == "O":
                queue.append((m-1, i))
                visited[m-1][i] = True
        
        # standard BFS, see where we can reach from the boundaries
        connections = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            cur_i, cur_j = queue.popleft()
            for d_i, d_j in connections:
                new_i, new_j = cur_i+d_i, cur_j+d_j
                if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] == "O" and not visited[new_i][new_j]:
                    visited[new_i][new_j] = True
                    queue.append((new_i, new_j))
        
        # go through the rest of the board, flip any cell not reachable from the boundary
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"