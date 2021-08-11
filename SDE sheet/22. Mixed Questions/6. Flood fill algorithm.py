"""
Given an image of size n*m, location of a pixel in the screen i,e(sr, cc) and color newColor, 
your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color newColor.
 

Example 1:

Input: image = {{1,1,1},{1,1,0},{1,0,1}},
sr = 1, sc = 1, newColor = 2.
Output: {{2,2,2},{2,2,0},{2,0,1}}
Explanation: From the center of the image 
(with position (sr, sc) = (1, 1)), all 
pixels connected by a path of the same color
as the starting pixel are colored with the new 
color.Note the bottom corner is not colored 2, 
because it is not 4-directionally connected to 
the starting pixel.

It is an extension to rotting oranges problem which we did in bfs and we have did this in dfs to increase our knowledge
"""
def floodFill(self, image, sr, sc, new):
    #Code here
    prev = image[sr][sc]
    def solve(image,sr,sc,new,prev):
        if sr < 0 or sc < 0 or sr >= n or sc >= m or image[sr][sc] != prev or image[sr][sc] == new:
            return
        image[sr][sc] = new
        
        solve(image,sr+1,sc,new,prev)
        solve(image,sr-1,sc,new,prev)
        solve(image,sr,sc+1,new,prev)
        solve(image,sr,sc-1,new,prev)
    solve(image,sr,sc,new,prev)
    return image
"""
TC = o(n*m)
SC = o(n*m)
"""