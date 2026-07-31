class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)==1 or len(strs)==0):
            return [strs]
        map1={}
        for string in strs:
            if("".join(sorted(string))  not in map1 ):
                map1["".join(sorted(string))]=[string]
            else:
                map1["".join(sorted(string))].append(string)
        return list(map1.values())            
            


