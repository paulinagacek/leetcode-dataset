class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:return False
        l=len(A)
        i,j=0,l-1
        while i<j and A[i]<A[i+1]:
            i+=1
        while j>0 and A[j]<A[j-1]:
            j-=1
        if i==j and j!=l-1 and i!=0:return True
        return False