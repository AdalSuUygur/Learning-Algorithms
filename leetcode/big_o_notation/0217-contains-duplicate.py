# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 10**5
# -10**9 <= nums[i] <= 10**5

#region Path II
#Runtime ms: 9
#Memory mb: 28.80
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums)) # Listenin boyu, kümenin boyundan büyükse demek ki bir şeyler silinmiş!
#endregion

#region Path I
#Runtime ms: 63
#Memory mb: 28.95
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         list_set_nums = list(set(nums)) #sete çevirdik ki tekrarlayan eleman varsa olmasın artık
#         if sorted(nums) == sorted(list_set_nums):
#             return False
#         else:
#             return True
#endregion