class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        arr.reverse()
        for i in range(len(arr)):
            for j in range(i):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]