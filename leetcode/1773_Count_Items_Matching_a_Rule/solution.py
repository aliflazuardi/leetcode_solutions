class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        t = 0
        match ruleKey:
            case "type":
                t = 0
            case "color":
                t = 1
            case "name":
                t = 2

        match_count = 0
        for item in items:
            if item[t] == ruleValue:
                match_count += 1

        return match_count
