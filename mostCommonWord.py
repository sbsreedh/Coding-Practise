
#One pass solution
#Tc:O(N+M)
#SC:O(N+M)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words=set(banned)
        ans=" "
        count=0
        word_count=defaultdict(int)
        words=[]
        for p,char in enumerate(paragraph):
            if char.isalnum():
                words.append(char.lower())
                if p!=len(paragraph)-1:
                    continue
            if len(words)>0:
                word="".join(words)
                if word not in banned_words:
                    word_count[word]+=1
                    if word_count[word]>count:
                        count=word_count[word]
                        ans=word
                words=[]
        return ans
  
  
  
  
#two pass solution:
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            string=" "
            for char in paragraph:
                if char.isalnum():
                    string+="".join(char.lower())
                else:
                    string+=" "
            # print(string)
            strings=string.split(" ")
            # print(strings)
            count=defaultdict()
            for x in strings:
                if x not in count:
                    count[x]=1
                else:
                    count[x]+=1
            
            counter=sorted(count.items(),key=lambda x:x[1],reverse=True)
            print(counter[1][0])
            for i in range(len(counter)):
                if counter[i][0]!="":
                    if counter[i][0] not in banned:
                          return counter[i][0]
