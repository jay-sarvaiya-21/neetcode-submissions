class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> h = new HashMap<>();
        for (int i=0; i < nums.length; i++){
            int comp = target - nums[i];
            if (h.containsKey(comp)){
                return new int [] {h.get(comp),i};
            }
            h.put(nums[i], i);
        }
    throw new IllegalArgumentException("No two sum solution");   
        
    }
}
