class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x : len(x))
        
        # strs 가 empty인 경우는 따로 처리
        if len(strs) ==0:
            return ""
        else:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]
