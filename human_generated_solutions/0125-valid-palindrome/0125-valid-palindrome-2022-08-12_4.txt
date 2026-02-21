def isPalindrome(self, s: str) -> bool:
        alnum = ""
        for letter in s:
            if letter.isalnum(): # checking for alphanumeric
                alnum += letter.lower()
        return alnum == alnum[::-1]