

import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        String str,rev="";
        int length,i;

        Scanner sc= new Scanner(System.in);
        System.out.println("Enter a string:");
        str=sc.nextLine();

        length=str.length();

        for(i=length-1;i>=0;i--)
            rev=rev+str.charAt(i);

            if(str.equals(rev))
                System.out.println(str+" is a palindrome");
            else
                System.out.println(str+" is not a palindrome");

    }
}
