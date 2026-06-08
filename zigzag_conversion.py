class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current = 0
        direction = 1

        for ch in s:
            rows[current] += ch

            if current == 0:
                direction = 1
            elif current == numRows - 1:
                direction = -1

            current += direction
        return "".join(rows)
        