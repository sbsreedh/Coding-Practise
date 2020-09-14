
#Trie implementation

class TrieNode:
    def __init__(self):
        self.children={}
        self.wordList=[]
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr.wordList.append(word)  
            curr=curr.children[c]
        curr.wordList.append(word)
    def search(self,word):
        res=[]
        curr=self.root
        for idx,c in enumerate(word):
            if c in curr.children:
                curr=curr.children[c]
                res.append(sorted(curr.wordList)[:3])
            else:
                for i in range(idx,len(word)):
                    res.append([])
                break
        return res
    
                    
                
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.insert(word)
        
        res = trie.search(searchWord)
        return res 
        
#String slicing solution:
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result=[]
        k=3
        sorted_arr=sorted(products)
        for i in range(len(searchWord)):
            res=[]
            for j in range(len(products)):
                  if searchWord[:i+1] ==sorted_arr[j][:i+1] and len(res)<3:
                        res.append(sorted_arr[j])
            result.append(res)
        return result
            
            
