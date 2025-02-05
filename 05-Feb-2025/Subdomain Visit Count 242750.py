# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        rees =[]
        for domains in cpdomains:
            fl = domains.split()
            num = fl[0]
            doma = fl[1].split(".")
            n = len(doma)
            for i in range(n):
                res = str(num) +" " + ".".join(doma[i:n])
                rees.append(res)
        c1 = defaultdict(int)
        for c in rees:
            c = c.split(" ")
            c1[c[1]] += int(c[0])
        print(c1)
        result = []
        for k, v in c1.items():
            result.append(str(v)+ " "+ str(k))
        return result