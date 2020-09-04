#Refernce: https://leetcode.com/problems/design-browser-history/discuss/675580/Python-simplest-and-most-optimal-beats-100-and-100-%2B-explanation
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curr=0

    def visit(self, url: str) -> None:
        self.curr+=1
        if self.curr==len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr]=url
            for _ in range(len(self.history)-self.curr-1):
                self.history.pop()

    def back(self, steps: int) -> str:
        self.curr=max(self.curr-steps,0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr=min(self.curr+steps,len(self.history)-1)
        return self.history[self.curr]
