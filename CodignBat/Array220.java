public class Array220 {
    public boolean array220(int[] nums, int index) {
        if (index + 1 >= nums.length) {
            return false;
        }
        return nums[index] * 10 == nums[index + 1] ? true :  array220(nums, index + 1);
    }
}
