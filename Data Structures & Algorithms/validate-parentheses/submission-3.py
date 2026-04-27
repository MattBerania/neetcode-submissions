class Solution:
    def isValid(self, s: str) -> bool:
        # LIFO : last in first out
        stack = []
        # Hash map to compare open to close
        closeToOpen = {")":"(","]":"[","}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    # If stack is true, meaning its not empty
                    # check if the last in stack is equal to the index c
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
    

        