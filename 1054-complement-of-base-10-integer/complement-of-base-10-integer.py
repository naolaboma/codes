class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bina = bin(n)[2:]
        res = ""
        for p in bina:
            if p == "1":
                res+="0"
            elif p == "0":
                res+="1"
        return int(res, 2)
        
