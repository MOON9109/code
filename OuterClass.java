package fastcampus.de.clip5;

public class OuterClass {

    public static void main(String[] args){
        System.out.println("outer class");
        InnerClass innerClass = new InnerClass();
        innerClass.printName();

    }
    public static class InnerClass {
        public void printName(){

            System.out.println(getClass().getName());
            System.out.println(this.getClass().getSimpleName());
        }

    }
}
