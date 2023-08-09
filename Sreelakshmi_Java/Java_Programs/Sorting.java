

public class Sorting {
    public static void main(String[] args) {
        int[] num = {1,3,4,5,0,6,7,7 };
        int i,j,temp;
        for(i=0;i<num.length;i++)
        {
            for(j=i;j<num.length;j++)
            {
                if(num[j]>=num[i])
                {
                    temp =num[j];
                    num[j]=num[i];
                    num[i]=temp;
                }
            }
        }
        for (int k : num
             ){
            System.out.println(k);
        }
    }
}
