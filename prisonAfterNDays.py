#1. create function next day , perform xor on adjacent prison cells and update
#2. create a visited dictionary to store the day we have operated on 
#3. if the day is not a fast forwarded one, N>0 then you go on decrementing by one and and do operation for next day prison cell arrangement and update the cells with next day rrangement
#4. If it fast forwarded, in the state keys, you store the present arrangement,
#5.then if the state key is present in seen dict, then calculate the cycle left as  as N%=seen[state_key]-N, and make fast forwarded a true else just update the seen by N
#6. return cells
#TC:O(min(N,2^k)
#SC:O(2^k)

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen=dict()
        fast_forwarded=False
        # convert to bitmap
        state_bitmap=0x0
        for cell in cells:
            state_bitmap<<=1
            state_bitmap=(state_bitmap|cell)
        while N>0:
            if not fast_forwarded:
                if state_bitmap  in seen:
                    N%=seen[state_bitmap]-N
                    is_fast_forwarded = True
                else:
                    seen[state_bitmap]=N
            if N>0:
                N-=1
                state_bitmap=self.next_day(state_bitmap)
        ret=[]
        for i in range(len(cells)):
            ret.append(state_bitmap & 0x1)
            state_bitmap = state_bitmap >> 1
        return reversed(ret)

    def next_day(self,state_bitmap):
            state_bitmap=~(state_bitmap<<1 )^(state_bitmap>>1)
            state_bitmap=(state_bitmap & 0x7e)
            return state_bitmap
            
 #TC:O(K.min(N,2^k)
#SC:O(K.2^k) 
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:          
            
        
        out=[0 for _ in range(len(cells))]
        # seen=dict()
        while N>0:
            N-=1
            for i in range(1,7):
                if cells[i-1]==0. and cells[i+1]==0 or cells[i+1]==1 and cells[i-1]==1:
                    out[i]=1
                else:
                    out[i]=0
                
            cells=list(out)
            # print("i")
            N=N%14
        return cells
    
