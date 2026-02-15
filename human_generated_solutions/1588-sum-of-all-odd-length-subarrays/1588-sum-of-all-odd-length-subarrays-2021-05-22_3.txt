class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
		#We declare our output variable with the initial value as the sum of all elements as this is the 1st iteration of the sum of all individual elements.
        result = sum(arr)
		#Saving length of the input array beforehand for ease of writing
        length = len(arr)
		#As we already summed up the individual elements, now its time to start groups starting from 3,5,7 and so onnn
        for j in range(3,length+1,2):
		#Now we need to create pairs for each element with the previous loop sizes
            for i in range(length):
			#This condition is to make we dont search for indexes outside our list
                if (i+j) > length:
                    break
					#We continously add the sum of each sublist to our output variable
                result += sum(arr[i:i+j])
        return result