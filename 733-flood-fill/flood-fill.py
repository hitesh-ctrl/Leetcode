class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        row = len(image)
        col = len(image[0])
        prevcolor = image[sr][sc]
        if color == prevcolor:
            return image

        def dfs(r,c):
            if(image[r][c] == prevcolor):
                image[r][c] = color
                if r>=1:dfs(r-1,c)
                if r+1<row:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<col:dfs(r,c+1)
        dfs(sr,sc)
        return image
