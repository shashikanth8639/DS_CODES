import java.util.*;

public class Input 
{
    Scanner sc = new Scanner(System.in);
    
    public int takeN()
    {
        System.out.println("Enter the number of elements");
        return sc.nextInt();
    }
    public int[] takeArray(int n)
    {
        int[] arr = new int[n];
        System.out.println("Enter the elements");
        for(int i=0; i<n; i++)
        {
            arr[i] = sc.nextInt();
        }

        return arr;
    }

    public int takeKey()
    {
        System.out.println("Enter the key to be searched");
        return sc.nextInt();
    }
    
}