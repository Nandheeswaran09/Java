public class missvalue {
    public static void main(String[] args) {
        int n = 6;
        int[] arr = { 1, 2, 3, 5, 6 };
        int sumn = (n * (n + 1)) / 2;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum = sum + arr[i];
        }
        int missvalue = sumn - sum;
        System.out.println("missvau" + missvalue);
    }
}
