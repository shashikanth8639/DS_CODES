import java.util.*;

public class binarySearch {
    public static void main(String[] args)
    {
        Input input = new Input();

        int n = input.takeN();
        int[] arr = input.takeArray(n);
        int key = input.takeKey();
        int start = 0,mid,end=n;
        
        Arrays.sort(arr);

        if(key < arr[0] || key > arr[n-1]){
            System.out.println("KEY NOT FOUND");
            return;
        }
        while(start < end)
        {
            mid = (start + end)/2;
            if(key == arr[mid]){
                System.out.println("KEY FOUND");
                return;
            }
            if(key < arr[mid]){
                end = mid;
            }else{
                start = mid+1;
            }
        }
        System.out.println("KEY NOT FOUND");
        return;
    }
}