class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res,sub=[],[]
        def dfs(i,target):
            if target==0:
                res.append(sub.copy())
                return
            for j in range(i,len(candidates)):
                if (j>i and candidates[j]==candidates[j-1]) :
                    continue
                if candidates[j]>target:
                    break
                sub.append(candidates[j])
                dfs(j+1,target-candidates[j])
                sub.pop()
        dfs(0,target)
        return res
