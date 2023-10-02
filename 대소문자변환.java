package org.example;



import java.util.Scanner;

class Main {
    public static void main(String[] args) {
//        System.out.println("Hello world!");
        Scanner sc =new Scanner(System.in);
        String str= sc.next();

        String answer="";

        for (int i=0 ; i<str.length(); i++){
            char ch = str.charAt(i);
            if (Character.isLowerCase(ch))
               answer=answer+Character.toUpperCase(ch);
            else answer=answer+Character.toLowerCase(ch);

        }
//        int B=sc.nextInt();
//        System.out.println(A+B);
        System.out.println(answer);
    }
}