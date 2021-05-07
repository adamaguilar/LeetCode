'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        for char1 in range(len(s)):
            unique = list()
            currentLongest = 0
            for char2 in range(char1, len(s)):
                if s[char2] not in unique:
                    unique.append(s[char2])
                    currentLongest = currentLongest + 1
                else:
                    break
            if currentLongest > longest:
                longest = currentLongest
        return longest

print(Solution().lengthOfLongestSubstring("abcabcbb"))