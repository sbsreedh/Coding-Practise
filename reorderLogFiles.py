#TC:O(M.N.logN), N is number of logs, sort()-takes O(N log N), comaprision takes O(M)
#SC:O(M.N)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        let_logs=[]
        dig_logs=[]
        for log in logs:
            if log.split()[1][0].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append(log.split(" ",1)[::-1])
        print(let_logs)
        let_logs.sort()
        # print(let_log)
        for idx,log in enumerate(let_logs):
            let_logs[idx]=log[1]+" "+log[0]
        return let_logs + dig_logs
            
      
