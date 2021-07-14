
import java.util.Scanner;
public class ReverseNumber {
    public static void main(String[] args) {
    int n,a;
    int s=0;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter any no: ");
        n=sc.nextInt();
        while(n>0){
            a=n%10;
            n=n/10;
            s=(s*10)+a;
        }
        System.out.println("reverse number is: "+s);

    }
}