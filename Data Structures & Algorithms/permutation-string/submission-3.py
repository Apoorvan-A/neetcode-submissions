class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l=0
        r=len(s1)-1
        if len(s1) > len(s2):
            return False
        s3=""
        for i in range(len(s1)):
            s3+=s2[i]

        while(r<= len(s2)-1):
            if(sorted(s3) == sorted(s1)):
                return True
            l+=1
            r+=1
            s3=s2[l:r+1]
        return False

            