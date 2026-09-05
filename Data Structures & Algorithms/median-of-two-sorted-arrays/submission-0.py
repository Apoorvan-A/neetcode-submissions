class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        print(i,j)
        while i<len(nums1):
            merged.append(nums1[i])
            i+=1
        while j<len(nums2):
            merged.append(nums2[j])
            j+=1
        length=len(merged)
        print(merged)
        if length%2==0:
            i1,i2=math.ceil(length/2),math.ceil(length/2)-1
            print(i1,i2)
            return (merged[i1]+merged[i2])/2
        else:
            return float(merged[length//2])