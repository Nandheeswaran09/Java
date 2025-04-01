class detail {
    private String name;
    int rollno;

    public void student() {
        System.out.println("--DEATILS--");
        System.out.println(name);
        System.out.println(rollno);
    }

    public void getvalue(String na, int ro) {
        name = na;
        rollno = ro;
    }

    public String get() {
        return nam;
    }
}

public class main {

    public static void main(String[] args) {
        detail de = new detail();
        de.getvalue("adf", 34);
        de.student();

    }
}