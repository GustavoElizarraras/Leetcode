class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        prefix = strs[0]
        for word in strs:
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix
                
            