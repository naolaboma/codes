class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        

        bins = ["", "", "", ""] # split IP address into 4 bins

        def validate(b: str) -> bool:
            if len(b) == 0:
                return False
            if len(b) > 1 and b[0] == "0":
                return False
            return int(b) <= 255

        ips = list()
        def formIP(i: int, j: int):
            # i indicates the i-th character of s
            # j indicates the j-th bin of bins
            if i >= len(s) and j < 3:
                # IP address not complete
                return
            if i == len(s) and j == 3 and validate(bins[3]):
                # got a valid IP address
                ips.append(".".join(bins))
                return
            if j > 3 or i >= len(s):
                return
            
            # put the i-th character to the j-th bin
            bins[j] += s[i] # do
            if validate(bins[j]):
                formIP(i+1, j)   # stay in this bin
                formIP(i+1, j+1) # move to the next bin
            bins[j] = bins[j][:-1] # undo

        formIP(0, 0)
        return ips