import java.util.Scanner;

public class BinaryToDecimal {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a Binary Number");
        String binaryString = sc.nextLine();
        System.out.println("Decimal Number: "+Integer.parseInt(binaryString,2));
    }
}

