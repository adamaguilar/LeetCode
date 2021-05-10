'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
'''

class Solution:
    def convert(self, s, numRows):
        numColumns = len(s) // numRows
        diagonal = 0
        if numRows > 2:
            diagonal = numRows - 2
        table = [["" for i in range(numColumns + (diagonal * numColumns) + 1)] for j in range(numRows)]
        for column in range(numColumns + (diagonal * numColumns) + 1):
            for row in range(numRows):
                if not s:
                    break
                elif column == 0 or numRows == 1 or column % (numRows - 1) == 0:
                    table[row][column] += s[0]
                    s = s[1:]
                else:
                    table[numRows - 1 - (column % (numRows - 1))][column] += s[0]
                    s = s[1:]
                    break
            if not s:
                break
        result = ""
        for n in range(len(table)):
            for n2 in range(len(table[n])):
                if table[n][n2]:
                    result += table[n][n2]
        return result

print(Solution.convert("test", "PAYPALISHIRING", 3))