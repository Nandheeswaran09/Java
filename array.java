public class array {
    public static void main(String[] args) {
        /*
         * int[] arr = new int[5];
         * arr[0] = 10;
         * arr[1] = 15;
         * arr[2] = 20;
         * arr[3] = 2;
         * arr[4] = 16;
         * int[] br = arr.clone();
         * br[2] = 11;
         * for (int i = 0; i < arr.length; i++) {
         * System.out.println(br[i]);
         * }
         */

        /*
         * int[] num = new int[50];
         * // int i = 1;
         * for (int i = 0; i < num.length; i++) {
         * i += 0;
         * System.out.println(i);
         * }
         */

        int mat[][] = new int[3][2];
        for (int i = 0; i < mat.length; i++) {
            i += 1;
            for (int j = 0; j < mat[0].length; j++) {
                j += 10;
                // mat[i][j]= i,j;
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }

    }
}
