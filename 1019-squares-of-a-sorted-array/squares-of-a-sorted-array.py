class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l,r = 0, len(nums)-1
        arr = []
        while l<=r:
            if abs(nums[l])<abs(nums[r]):
                arr.append(nums[r]**2)
                r-=1
            else:
                arr.append(nums[l]**2)
                l+=1
        return arr[::-1]
        