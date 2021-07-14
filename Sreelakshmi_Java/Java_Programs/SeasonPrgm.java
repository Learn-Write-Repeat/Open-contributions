

import java.util.Scanner;

public class SeasonPrgm {

    public static void main(String[] args) {
    String season;
    int sea;
        System.out.println("Enter any month (1 to 12)");
        Scanner sc = new Scanner(System.in);
        sea=sc.nextInt();
        switch (sea)
        {
            case 12:
            case 1:
            case 2:
                season= "winter";
                break;
            case 3:
            case 4:
            case 5:
                season= "spring";
                break;
                case 6:
                case 7:
                case 8:
                    season= "summer";
                    break;
            case 9:
            case 10:
            case 11:
                season= "autumn";
                break;
            default:
                season= "bogus month";
        }
        System.out.println("The entered month is in the "+season+".");
    }
}
