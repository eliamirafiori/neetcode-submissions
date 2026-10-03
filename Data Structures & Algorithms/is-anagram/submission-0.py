class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = {}
        t_list = {}

        for c in s:
            if c not in s_list:
                s_list.update({c:0})

            s_list[c] += 1

        for c in t:
            if c not in t_list:
                t_list.update({c:0})
            t_list[c] += 1 

        if s_list == t_list: return True

        return False

