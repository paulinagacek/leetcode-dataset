class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l=len(str(low))
        h=len(str(high))
        ans=[]
        a=[12,23,34,45,56,67,78,89]
        t=0
        while l<=h:
            for i in a:
                for j in range(0,l-2):
                    t=i%10
                    if i==9:
                        break
                    i=int(str(i)+str(t+1))
                if i%10==0:
                    break
                if i>=low and i<=high:
                    ans.append(i)
            l+=1
        return ans