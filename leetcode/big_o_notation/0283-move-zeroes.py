#283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

#runtime ms: 3
#runtime mb: 18.72
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0 # Sıfır olmayan sayıyı nereye koyacağımızı tutan işaretçi

        for i, num in enumerate(nums): #listeyi en baştan sona doğru çekiyorum, indexe de ihtiyacım olduğu için enumerate kullandım
            if num != 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        return nums