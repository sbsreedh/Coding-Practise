#TC:O(N)
#SC:O(N)
#Use Stack(s) to save adjacent duplicate chars and the corresponding occurrences, pop them out when the occurrences reach k;
#Build String by the items remaining in Stack(s).
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        res=""
        
        for s in S:
            if not stack:
                stack.append([s,1])
                continue
      
            prev,count=stack[-1]
            # print(prev,count)
            if prev==s :
                stack.append([s,count+1])
                
            elif prev!=s:
                stack.append([s,1])
            # print("stack",stack)
            if stack[-1][1]>1:
                stack=stack[:-stack[-1][1]]
        
        for letter,val in stack:
            # print(letter)
            res+="".join(letter) 
        return res
        # return  ''.join(map(lambda x: x[0], stack))
                
