class Solution:
    def trap(self, height: List[int]) -> int:
        #2 arrays to calc max element to the right at any index, and left
        # iterate through height array, compute # num water with 
        # min(max to left, msx to right) - curr index height
        # return this sum 

        # [3, 3, 3, 3, 3, 3, 3, 2, 1, 0] right
        # [0, 0, 2, 2, 3, 3, 3, 3, 3, 3] left

        # 
        
        left, right = [0], [0]

        currMax_left = 0
        for i in range(1, len(height)):
            if height[i - 1] > currMax_left:
                left.append(height[i - 1])
                currMax_left = height[i - 1]
            else:
                left.append(currMax_left)
        
        currMax_right = 0
        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > currMax_right:
                right.append(height[i + 1])
                currMax_right = height[i + 1]
            else:
                right.append(currMax_right)
        right = right[::-1]
        res = 0


        for i in range(len(height)):
            
            res += max(min(left[i], right[i]) - height[i], 0)
       


        return res



