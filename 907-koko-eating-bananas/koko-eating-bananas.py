import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left=1
        right=max(piles)
        ans=right

        while(left <= right):
            k=(left+right)//2

            hours_needed = 0
            for p in piles:
                hours_needed+=math.ceil(float(p)/k)
            if (hours_needed <= h):
                ans=k
                right = k-1
            else:
                left = k+1
        return ans