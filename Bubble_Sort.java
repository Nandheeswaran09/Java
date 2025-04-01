public class Bubble_Sort {
    public static void main(String[] args) {
        int[] nums = { 6, 7, 3, 2, 4, 5 };
        int temp;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
        for (int num = 0; num < nums.length; num++) {
            System.out.print(nums[num] + " ");
        }
    }

}
