# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?



#region solution 1
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         else:
#             return False
#endregion

#region solution 2
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         count = {} # Notlarındaki boş sözlük tanımı
#         # s kelimesindeki harfleri sayalım
#         for char in s:
#             # Eğer char yoksa varsayılan olarak 0 döndürür
#             count[char] = count.get(char, 0) + 1 # CRUD: Update veya Create
#         # t kelimesindeki harfleri sözlükten düşelim
#         for char in t:
#             if char not in count or count[char] == 0:
#                 return False
#             count[char] -= 1 # Değeri bir azalt
#         return True
    
#endregion

#region solution 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        if len(s) != len(t):
            return False
        else:
            for letter in s: # s içerisindeki her bir harfi gez
                if letter in letters: #sözlük içerisinde bu harf varsa
                    letters[letter] += 1 #sözlükteki value'sunu 1 azalt
                else:
                    letters[letter] = 1 #yoksa da sözlüğe ekle.

            for letter in t:
                if letter not in letters or letters[letter] == 0: #eğer key olarak letters içinde yoksa veya artık sıfırlandıysa
                    return False
                else:
                    letters[letter] -= 1
            return True
#endregion

# (letters[letter] = 1 if letter not in letters else letters[letter] += 1 for letter in s) bu yöntem çalışmadı
# for letter in s:
    # "letter"ı getir, bulamazsan 0 kabul et ve üzerine 1 ekle.
    # letters[letter] = letters.get(letter, 0) + 1
    # çalışan yöntem bu
