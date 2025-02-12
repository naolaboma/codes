# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r=0,len(skill)-1
        summ = 0
        while l<r:
            if skill[l]+skill[r] != skill[0]+skill[len(skill)-1]:
                return -1
            summ+=skill[l]*skill[r]
            l+=1
            r-=1
        return summ