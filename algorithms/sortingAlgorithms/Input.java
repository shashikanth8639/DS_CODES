import java.util.*;

public class Input
{
	Scanner sc = new Scanner(System.in);
	public int takeN()
	{
		System.out.println("Enter the number of elements to be sorted");
		return sc.nextInt();
	}

	public int[] takeArray(int n)
	{
		int[] arr = new int[n];
		System.out.println("Enter the array elements to be sorted");
		for(int i=0; i<n; i++)
		{
			arr[i] = sc.nextInt();
		}
		return arr;
	}

	public void print(int[] arr)
	{
		System.out.println("After sorting the array, elements are: ");
		for(int i=0; i<arr.length; i++)
		{
			System.out.print(arr[i]+" ");
		}
		System.out.println();
	}

}