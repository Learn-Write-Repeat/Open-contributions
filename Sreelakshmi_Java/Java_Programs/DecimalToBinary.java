
import java.util.Scanner;
import java.util.Stack;

public class DecimalToBinary {
    public static void main(String[] args) {
        int num;
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack= new Stack<Integer>();
        System.out.println("Enter Decimal number: ");
        num = sc.nextInt();
        while (num!=0){
            int d = num%2;
            stack.push(d);
            num=num/2;
        }
        System.out.println("\nBinary representation is: ");
        while(!(stack.isEmpty())){
            System.out.println(stack.pop());

        }
        System.out.println();
    }
}
