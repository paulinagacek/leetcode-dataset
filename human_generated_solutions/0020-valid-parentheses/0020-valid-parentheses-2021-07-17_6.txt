class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        Runtime: 4 ms, faster than 99.98% of Python online submissions for Valid Parentheses.
        Memory Usage: 13.5 MB, less than 59.39% of Python online submissions for Valid Parentheses.
        """
        ##Mapping the Parentheses
        m = {\'(\' : \')\', \'[\': \']\', \'{\': \'}\'}
        ##Adding the expected values to stack
        stack = []
        
        ##Iterating through the input array
        for i in s:
            ## cheacking if the value in the map
            if i in m:
                ## append to stack the expected values
                stack.append(m[i])
            ##If not, then we check if the stack is not empty and that the value matches the last value added to the stack
            elif len(stack) > 0 and i == stack[-1]:
                ## if true, then we pop it (remove it)
                stack.pop()
            else:
                ## if none of the cases matches then we just return false
                return False
        ## if all the data in stack is popped then we just compare the length of stack to 0 (there should be no element left)
        return len(stack) == 0