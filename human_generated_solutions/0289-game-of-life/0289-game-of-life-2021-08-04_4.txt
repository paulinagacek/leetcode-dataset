class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbours = []
                if j!=0 and i!=0:
                    neighbours.append(board[i-1][j-1] % 2)
                if j != len(board[0])-1 and i != len(board) -1 :
                    neighbours.append(board[i+1][j+1])
                if j!=len(board[0])-1 and i!=0:
                    neighbours.append(board[i-1][j+1] % 2)
                if j!=0 and i!=len(board)-1:
                    neighbours.append(board[i+1][j-1])
                
                if i !=0:
                    neighbours.append(board[i-1][j] % 2)
                if i != len(board)-1:
                    neighbours.append(board[i+1][j])
                if j !=0:
                    neighbours.append(board[i][j-1] % 2)
                if j!=len(board[0])-1:
                    neighbours.append(board[i][j+1])
                    
                oneCount = neighbours.count(1)
                if oneCount < 2:
                    board[i][j] = 0 if board[i][j]==0 else 1
                elif oneCount == 2:
                    board[i][j] = 0 if board[i][j]==0 else 3
                elif oneCount > 3:
                    board[i][j] = 0 if board[i][j]==0 else 1
                elif oneCount == 3:
                    board[i][j] = 2 if board[i][j]==0 else 3
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] // 2