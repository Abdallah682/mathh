class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s=""
        for i in digits:
            s+=str(i)
        n=str(int(s)+1)
        digits=[]
        for i in n:
            digits.append(int(i))
        return digits