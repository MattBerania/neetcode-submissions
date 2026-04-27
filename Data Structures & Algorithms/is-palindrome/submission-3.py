class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            two-pointer approach
            iterate through the list at most once
            O(1) means not creating any data for storage
        '''
        # get rid of spaces
        s = s.replace(" ", "")
        
        left = 0
        right = len(s)-1


        # "abba", "aba"
        while left < right+1:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True



