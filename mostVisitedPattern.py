class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        history=defaultdict(list)O(mXN)
        for u,t,w in sorted(zip(username,timestamp,website)):#O(N)
            history[u].append(w)
        count=defaultdict(int)O(mxN)
        for users,webs in history.items():#O(N)
            comb=set(combinations(webs,3))
            for c in comb:
                # print(c)
                count[tuple(c)]+=1
        result=None
        maxCount=0
        for pattern , cnt in count.items():#O(N)
                
            if cnt>maxCount or (cnt == maxCount and pattern<result ):
                maxCount=cnt
                result=pattern
        return result
            
            
