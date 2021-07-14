

import java.util.Scanner;

import static java.lang.Math.sqrt;

public class PrimeNumbers {
    public static void main(String[] args) {
        int i,f,n;
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter you number:");
        n = sc.nextInt();
        f=1;
        for(i=2;i<=sqrt(n);i++)
            if(n%i==0){
                f=0;
                break;
            }
            if(f==1)
                System.out.println(n+ " is prime number");
             else
                System.out.println(n+ " is not a prime number");
    }
}
