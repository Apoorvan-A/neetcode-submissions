class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ls_str=[str(dig) for dig in digits]
        str_dig="".join(ls_str)
        dig=int(str_dig)
        dig+=1
        return list(str(dig))