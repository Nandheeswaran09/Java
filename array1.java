public class array1 {
    public static void main(String[] args) {
        // single dimension array
        int[] num = new int[6];
        int a = 1;
        for (int i = 0; i < num.length; i++) {
            num[i] = a + 1;
            a = num[i];
        }
        // System.out.println(num[2]);

        // mutli-demision array
        int[][] nums = new int[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                nums[i][j] = j + 1;
                System.out.print(nums[i][j] + " ");
            }
            System.out.println();
        }
    }
}