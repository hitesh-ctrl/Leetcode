class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        width = len(height)
        area = 0
        
        l,r= 0, len(height)-1
        while l<r:
            if height[l]<height[r]:
                area = max(area,(height[l]*(r-l)))
                l+=1
            else:
                area = max(area,(height[r]*(r-l)))
                r-=1
        return area



                
        