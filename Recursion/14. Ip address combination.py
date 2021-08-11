"""
Given a string of digits ip, generate all possible valid IP address combinations and return them in sorted order.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are integers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

Constraints

4 ≤ n ≤ 12 where n is the length of ip.
Example 1
Input
ip = "2542540123"
Output
["254.25.40.123", "254.254.0.123"]
"""
class Solution:
    
    def solve(self, ip):
        ans = []
        def s(ip,op,count):
            nonlocal ans
            if len(ip) == 0:
                ans.append(op)
                return 
            if count == 0:
                if ip:
                    op += ip
                    ans.append(op)
                return
            for i in range(len(ip)):
                s(ip[i+1:],op+ip[:i+1]+".",count - 1)
        s(ip,"",3)
        final = []
        for i in ans:
            if i[-1] != ".":
                tmp = i.split(".")
                flag = True
                for j in tmp:
                    if j[0] == "0" and len(j) > 1:
                        flag = False
                        break
                    elif int(j) < 0 or int(j) > 255:
                        flag = False
                        break
                if flag:
                    final.append(i)
        return final
                    

        
