class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> hashMap=new HashMap<>();
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(hashMap.containsKey(nums[i])){
                return true;
            }
            else{
                hashMap.put(nums[i],i);
            }
        }
        return false;
    }
}