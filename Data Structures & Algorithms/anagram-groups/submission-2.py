class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq={}
        for string in strs:
            count=[0]*26
            for ch in string:
                count[ord(ch)-ord('a')]+=1
            count=tuple(count)
            if count in freq:
                freq[count].append(string)
            else:
                freq[count]=[string]
        return list(freq.values())