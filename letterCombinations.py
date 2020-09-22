#Backtracking solution
#TC:O(3^nx4^m)=SC,n-3 letter mapping, m-4 letters mapping
# If there is no more digits to check that means that the current combination is done.
# If there are still digits to check :
# Iterate over the letters mapping the next available digit.
# Append the current letter to the current combination combination = combination + letter.
# Proceed to check next digits : backtrack(combination + letter, next_digits[1:]).


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={"2":"abc",
                "3":"def",
                "4":"ghi",
                 "5":"jkl",
                "6": "mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"}
        res=[]
        def helper(combination,next_digits):
            if len(next_digits)==0:
                res.append(combination)
            else:
                for letter in letters[next_digits[0]]:
                    helper(combination+letter,next_digits[1:])
        if digits:
            helper("",digits)
        return res
             
