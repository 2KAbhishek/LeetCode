class Solution {
    public int[] twoSum(int[] nums, int target) {

        if (nums.length > 2){

            HashMap <Integer, Integer> hmap = new HashMap<>();
            k
            for (int i = 0; i < nums.length; i++){
                if (!hmap.isEmpty() && hmap.containsKey(target - nums[i])){
                    return new int[] {hmap.get(target - nums[i]), i};
                } else hmap.put(nums[i], i);
            }
        }

        return new int[] {0,1};
    }
}

