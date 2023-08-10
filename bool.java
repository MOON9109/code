package fastcampus.de.clip7;

public class bool {

    public static void main(String[] args) {
        boolean fact = true;
        System.out.println(fact);
        System.out.println("true");


        Defaults defaults= new Defaults();
        System.out.println(defaults.booleanDefault);

    }

    static class  Defaults{


        boolean booleanDefault;
    }
}
