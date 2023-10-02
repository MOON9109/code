package org.example;



import java.util.Scanner;

class Main {
    public static void main(String[] args) {
//        System.out.println("Hello world!");
        Scanner sc =new Scanner(System.in);
        char [] first_string = sc.nextLine().toCharArray();
        char [] second_string = sc.nextLine().toCharArray();
        int [] Alpha =new int[26];
        int alpha_num_first=0;
        int alpha_num_second=0;
        for (int i=0 ; i< first_string.length;i++)
        {
            alpha_num_first=first_string[i]-'a';
            Alpha[alpha_num_first]=Alpha[alpha_num_first]+1;
        }

        for (int i=0 ; i< second_string.length;i++)
        {
            alpha_num_second=second_string[i]-'a';
            Alpha[alpha_num_second]=Alpha[alpha_num_second]-1;
        }

        int result=0;

        for (int i=0 ; i< Alpha.length;i++){

            int alpha_count=Math.abs(Alpha[i]);

            if (alpha_count!=0)
                result=result+alpha_count;



        }
        System.out.println(result);

//        String second_string = sc.next();




    }
}