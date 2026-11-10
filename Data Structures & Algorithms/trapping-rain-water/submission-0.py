class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        left_max =0
        right_max =0
        total = 0

        while left < right:
            if height[left] <height[right]:
                left_max = max(left_max, height[left])
                l = left_max - height[left]
                total += l
                left +=1
            else :
                right_max = max(right_max , height[right])
                r= right_max - height[right]
                total += r
                right -= 1
        return total



