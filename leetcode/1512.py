# 1512. Number of Good Pairs

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0

# enumerate

# hem index küçük mü bakıcaz
# hem de değer aynı mı diye bakıcaz

#valueları bğirbirlerine eşit olanları çekjicez
#index değerlerine bakıcaz
#indexi küçük olanları kabul edicez
#çıktımızda ise index değerini ikisinin alıp yen ibir şekilde yazdırıp kabul sayıcaz

# nums = [1,2,3,1,1,3]

# for index, value in enumerate(nums):
#     print(index, value)


