# Given a number N, write an algorithm to print character ‘A’ exactly N times with minimum no of operations (either copy all or paste)

public class MinimumCopyPasteDP {  //bankManager
    public int find(int number){
        int res = 0;
        for(int i=2;i<=number;i++){
            while(number%i == 0){ //check if problem can be broken into smaller problem
                res+= i; //if yes then add no of smaller problems to result. If number = 25  i = 5 then 5*5 = 25 so add 5 to results
                number=number/i; // create smaller problem
            }
        }
        return res;
    }

    public static void main(String[] args) {
        MinimumCopyPasteDP m = new MinimumCopyPasteDP();
        int n = 6;
        System.out.println("Minimum Operations: " + m.find(n));

    }
}

