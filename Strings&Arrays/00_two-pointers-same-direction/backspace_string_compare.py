"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""
class Solution():
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(st):
            left = 0
            st = list(st)
            for right in range(len(st)):
                if st[right] == "#":
                    if left > 0:
                        left -= 1
                else:
                    st[left] = st[right]
                    left += 1
            return st[:left]
        return build(s) == build(t)

if __name__ == "__main__":    
    s = "ab#c"
    t = "ad#c"
    solution = Solution()
    print(solution.backspaceCompare(s, t))