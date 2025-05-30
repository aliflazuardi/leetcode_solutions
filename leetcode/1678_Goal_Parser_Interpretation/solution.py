class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                ans += "G"
                i += 1
                continue
            if command[i + 1] == ")":
                ans += "o"
                i += 2
                continue
            ans += "al"
            i += 4

        return ans
