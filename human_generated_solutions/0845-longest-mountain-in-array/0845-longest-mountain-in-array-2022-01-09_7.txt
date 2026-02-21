class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maxlen = 0
        n = len( arr)
        maxi = 0
        tp = 0
        incFlag = 0
        decFlag = 0
        if n < 3:
            return 0

        for i in range (2,n):
            prev = arr[i-1]    
            prevprev = arr[i-2]    
            # print( tp)
            if prevprev < prev and prev < arr[i]:
                if tp == 0:
                    tp = 2
                tp += 1
                incFlag = 1
            elif decFlag != 1 and prevprev < prev and prev > arr[i]:
                if incFlag == 0:
                    incFlag = 1
                    tp += 2
                tp += 1
                decFlag = 1
                # if incFlag == 1 and decFlag == 1:
                maxlen = max( maxlen, tp)
            elif incFlag == 1 and decFlag == 1 and prevprev > prev and prev > arr[i]:
                tp += 1
                # decFlag = 1
                # if incFlag == 1 and decFlag == 1:
                maxlen = max( maxlen, tp)
            else:
                incFlag = 0
                decFlag = 0
                tp = 0
            print( tp)
        return maxlen