class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l=0
        r=len(nums)-1

        def f(arr,start,end,target):

            if start>end:
                return -1
            mid=start+(end-start)//2

            if(nums[mid])==target:
                return mid
            
            elif(nums[mid]<target):
                return f(arr,mid+1,end,target)
            
            else:
                return f(arr,start,mid-1,target)
            return -1
        return f(nums,l,r,target)

