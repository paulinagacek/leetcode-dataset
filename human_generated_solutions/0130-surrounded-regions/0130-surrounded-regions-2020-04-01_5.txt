class Solution:
    
    def dfs(self,board,i,j):
            
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=\'O\':
            return
        board[i][j]=\'$\'  # converting to  a dollar sign 
            
        self.dfs(board,i+1,j)
        self.dfs(board,i-1,j)
        self.dfs(board,i,j+1)
        self.dfs(board,i,j-1)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return None
        
        m=len(board)
        n=len(board[0])
        
        
        for i in range(m):  # call dfs on all border \'O\'s and turn them to \'$\'
            for j in range(n):
                if i==0 or i==m-1:
                    self.dfs(board,i,j)
                        
                if j==0 or j==n-1:
                    self.dfs(board,i,j)
                    
        
   
#all border O and others connected them were already converted to $ sign 
#so left out zeros are surely surrounded by \'X\' . Turn all of them to \'X\'
        for i in range(m):   
            for j in range(n):
                if board[i][j]==\'O\':
                    board[i][j]=\'X\'
        
# turn the border zeros and their adjacents to their initial form. ie $ -> O 
        for i in range(m):
            for j in range(n):
                if board[i][j]==\'$\':
                    board[i][j]=\'O\'