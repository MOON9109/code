package fastcampus.de.clip7;

;

public class character {
    public static void main(String[] args) {

        char alphabet ='A';
        System.out.println(alphabet);




        System.out.println("================= default ============");

        Defaults defaults = new Defaults();

        System.out.println(defaults.charDefault);
        System.out.println(defaults.intDefault);
        System.out.println(defaults.shortDefault);
        System.out.println(defaults.longDefault);
        System.out.println(defaults.doubleDefault);




    }

    static class Defaults {
        char charDefault;

        short shortDefault;
        int intDefault;
        long longDefault;
        double doubleDefault;


    }
}
