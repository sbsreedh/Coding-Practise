#TC:O(n^2+n+w)
#SC:O(n^2.n+W)#clarify from solution
#create a hasset to store the words in dictionary
#create a map to track which word yu are starting with. 
#then recursively call to find if the successive words are present in the dict or not.
#return the word


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
            wordset=set(wordDict)
            hashMap=defaultdict(list)
            def recurse(s):
                if not s:
                    return [[]]
                if s in hashMap:
                    return hashMap[s]
                for i in range(1,len(s)+1):
                    word=s[:i]
                    # print(word)
                    if word in wordset:
                        for nextwords in recurse(s[i:]):
                            hashMap[s].append([word]+nextwords)
                            print(hashMap[s])
                return hashMap[s]
            recurse(s)
            return [" ".join(words) for words in hashMap[s]]

         
