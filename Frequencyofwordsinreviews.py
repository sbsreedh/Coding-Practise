#https://leetcode.com/discuss/interview-question/542597/
# print("Hello World!")


#preprocess to convert everything to lower case
def preprocess(word):
    res=""
    for c in word:
        if c not in string.punctuation:
            res+=c.lower()
    return res
def freq(reviews,keywords,k):
    count={}
    
    kw=set([w.lower() for w in keywords ])
    for review in reviews:
        seen=set()#once per review
        words=review.split(" ")
        for word in words:
            w=preprocess(word)
            if w in kw and w not in seen:
                count[w]=count.get(w,0) + 1
                seen.add(w)
    sorted_arr=sorted(count.keys(),key=lambda x:(-count[x],x))
    print( sorted_arr[:k])
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
k=2
freq(reviews,keywords,k)

        
