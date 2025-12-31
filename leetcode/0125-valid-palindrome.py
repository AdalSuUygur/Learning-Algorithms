# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

#region Path I
#runtime ms: 3
#memory mb: 18.56
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import string
#         a = s.lower().replace(" ", "")
#         b = "".join(ch for ch in a if ch not in string.punctuation)
#         return b[::-1] == b
#endregion

#region Path II
#runtime ms: 3
#memory mb: 18.56
class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_str = "".join([ch.lower() for ch in s if ch.isalnum()]) #eğer alfanumerikse küçült ve stringe ekle.
        return only_str[::-1] == only_str
#endregion
