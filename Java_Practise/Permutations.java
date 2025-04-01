public class Permutations {

    public static void permute(int[] arr, int start) {

        if (start == arr.length - 1) {
            for (int num : arr) {
                System.out.print(num + ' ');
            }
            System.out.println();
        } else {
            for (int i = start; i < arr.length; i++) {
                swap(arr, start, i);
                permute(arr, start + 1);
                swap(arr, start, i);
            }
        }

    }

    public static void swap(int[] arr, int i, int j) {

        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };
        permute(arr, 0);
    }
}
