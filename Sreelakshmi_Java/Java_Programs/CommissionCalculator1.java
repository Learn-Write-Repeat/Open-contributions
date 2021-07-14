import java.util.Scanner ;

public class CommissionCalculator3 {

        public static void main(String[] args)
        {
            // define variables & initialize them
            double salary = 50000.00 ;   // Salesperson fixed salary $50000
            double rate = .05 ;         // Salesperson commission rate 5%
            double annual;       // Inputted annual sales
            double compensation;    // Annual compensation
            double target= 120000;   // Target sales
            double acceleration = .015; // Acceleration factor for sales over $120,000
            double rate2 = .08;  // Sales incentive starts when 80% of sales target is met.

            // Output message for user to input annual sales
            System.out.println("Please input annual sales: ") ;
            Scanner input = new Scanner(System.in) ;
            annual = input.nextDouble() ;
            compensation = annual * rate + salary ;

            // Output information for user to receive annual compensation information
            System.out.println("Your annual compensation is: " + compensation) ;

            // Output information for displaying the table of potential total annual
            // compensation.
            System.out.println("Total Sales\t\t\tTotal Compensation");
            System.out.println("------------------------------------");

            {
                if(annual <= 80.0 * target/100.0)
                    compensation = 0;
                else if(annual <= target)
                    if(annual == 25.0 * target / 100.0);
                    else compensation = 25.0 * annual / 100 + rate2 * annual;
            }

        }
    }

