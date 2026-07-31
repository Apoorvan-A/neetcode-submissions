class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1={}

        for string in strs:
            l=[0]*26
            for i in string:
                l[ord(i)-ord('a')]+=1
            map1.setdefault(tuple(l),[]).append(string)
        return list(map1.values())

