package javapackage1;

import java.util.Scanner;

public class FiboFunc {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("\n Enter the length of the sequence: ");
		int num = sc.nextInt();
		
		//method call
		displayfibo(num);
		sc.close();
	}

		static void displayfibo(int n){
		    int x = 1, y = 0, z = 0, count = 1;
		    while(count<=n){
		        System.out.print(z + "   ");
		        z = x + y;
		        x = y;
		        y = z;
		        count++;
		    }

	}

}
