 /**
     * Write a java program that counts the commission of a salesman as
     * following:
     * If the Total Sales is equal or grater than 1000 the commission rate will be
     * 8% otherwise it will be 0.
     * Your program should ask the user to enter the total sales and then print the
     * total commission.
     **/

import java.util.Scanner;

public class CommissionOfSalesman {

   

    public static void main(String[] args) {
    double commissionRate = 0.0;
    double TotalSales , Commission;

    Scanner sc= new Scanner(System.in);
        System.out.println("please enter the total sales ");
        TotalSales=sc.nextDouble();

        if(TotalSales>=1000) {
            commissionRate = 0.08;
            Commission = commissionRate * TotalSales;

            System.out.println("the commission is : " + Commission);
        }
            else{
                System.out.println("no commission for under 1000");
            }
        }
    }
