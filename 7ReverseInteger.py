'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution:
    def reverse(self, x):
        if x <= -(2 ** 31) or x >= ((2 ** 31) - 1):
            return 0
        positive = True
        if x < 0:
            x = x * -1
            positive = False
        position = len(str(x)) - 1
        result = 0
        while x != 0:
            result = result + ((x % 10) * 10 ** position)
            x = x // 10
            position = position - 1
        if not positive:
            result = result * -1
        if result <= -(2 ** 31) or result >= ((2 ** 31) - 1):
            return 0
        return result

print(Solution.reverse("test", -321))