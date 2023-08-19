import java.util.*;
class Main{
    public String solution (String str){
        String answer="";

        for (char x : str.toCharArray()){

            if (Character.isLowerCase(x)) answer+=Character.toUpperCase(x);
            else answer+=Character.toLowerCase(x);
        }

        return answer;



    }

    public static void main(String[] args) {
        Main T= new Main();
        Scanner kb = new Scanner(System.in);
        String str=kb.next();
//        char c=kb.next().charAt(0);
        System.out.print(T.solution(str));
    }

}
