class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isperm(s1,s2):
            count1,count2=[0]*26,[0]*26
            for i in range(len(s1)):
                count1[ord(s1[i])-ord("a")]+=1
                count2[ord(s2[i])-ord("a")]+=1
            return count1==count2
        l=0
        r=len(s1)-1
        if len(s1) > len(s2):
            return False
        s3=""
        for i in range(len(s1)):
            s3+=s2[i]

        while(r<= len(s2)-1):
            if(isperm(s3,s1)):
                return True
            l+=1
            r+=1
            s3=s2[l:r+1]
        return False

            