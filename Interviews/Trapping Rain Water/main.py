class Solution(object):
    def trap(self, height):
        if 0 == len(height):
            return 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        res = 0
        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
        


if "__main__" == __name__:
    s = Solution()
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(arr    ))