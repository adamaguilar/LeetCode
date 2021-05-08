'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s):
        possible = set()
        longest = s[0]
        for char1 in s:
            char = char1
            possible.add(char)
            s = s[1:]
            for char2 in s:
                char = char + char2
                possible.add(char)
        for string in possible:
            if len(string) > len(longest):
                for x in range(len(string) // 2):
                    if string[x] != string[-x - 1]:
                        break
                if len(longest) < len(string) and string[x] == string[-x - 1]:
                    longest = string
        return longest

print(Solution.longestPalindrome("test", "babad"))