class Solution(object):
    def find(self,arr,target):
        dct={0:1}
        s,c=0,0
        for i in range(len(arr)):
            s+=arr[i]
            if (s-target) in dct:
                c+=dct[s-target]
            if s not in dct:
                dct[s]=0
            dct[s]+=1
        return c
    def numSubmatrixSumTarget(self, matrix, target):
        n,m=len(matrix),len(matrix[0])
        ind=0
        count=0
        while ind<m:
            arr=[0]*n
            for j in range(ind,m):
                for i in range(n):
                    arr[i]+=matrix[i][j]
                count+=self.find(arr,target)
            ind+=1
        return count