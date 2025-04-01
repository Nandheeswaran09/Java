
class Solution {

    enum fruits {
        apple, mango, orange;
    }

    public static void main(String[] args) {

        for (Object o : fruits.values()) {
            System.out.println(o);
        }
        fruits f1 = fruits.apple;
        System.out.println(f1);
        final int val1 = 23;
        // byte stores from -128 to 127
        byte val = 24;
        System.out.println("Hello World" + val + val1);
    }
}