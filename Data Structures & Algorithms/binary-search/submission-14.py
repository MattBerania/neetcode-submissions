class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ascending order
        # target integer
        '''
            FUNCTION:
            if the target < nums[mid] 
        '''
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            if nums[0] == target: return 0
        elif len(nums)==2:
            if nums[0] == target: 
                return 0
            elif nums[1] == target: 
                return 1

        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r)//2
            # check if l or r is == target
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            # Check the middle
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return -1    


