#TC:O(N)
#SC:O(N)

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0
        stack=[]
        count=0
        res=0
        if S[0]=="(":
            stack.append(S[0])
        else:
            count=1
        for i in range(1,len(S)):
            if S[i]=="(":
                stack.append(S[i])
            elif S[i]==")":
                if stack:
                    if stack[-1]=="(" :
                        stack.pop()
                elif len(stack)==0:
                        count+=1
        res=count+len(stack)
        return res
                
class Solution(object):
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
    
                
