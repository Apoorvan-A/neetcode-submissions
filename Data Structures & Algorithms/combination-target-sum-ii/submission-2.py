class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtrack(idx,subset,current_sum):
            if current_sum==target:
                res.append(subset.copy())
                return
            
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]+current_sum>target :
                    return 
                subset.append(candidates[i])
                backtrack(i+1,subset,current_sum+candidates[i])
                subset.pop()
        backtrack(0,[],0)
        return res