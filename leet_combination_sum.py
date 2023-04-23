class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        value_list=[]
        res=[]
        def dfs (value_list,candidates):
            if sum(value_list)==target:
                res.append(value_list)
                return
            elif sum(value_list)>target:
                return

            else:
                for i , value in enumerate(candidates):
                    dfs( value_list+[value],candidates[i:])

        dfs(value_list, candidates)
        return res
