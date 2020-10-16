import java.util.*;

public class SelectionSort
{
	public static void main(String[] args)
	{
		Input input = new Input();

		int n = input.takeN();
		int[] arr = input.takeArray(n);

		selectionSort(arr, n);

		input.afterSorting(arr);
		
		return;
	}

	static void selectionSort(int[] arr, int n)
	{
		int j,tmp;
		for(int i=0; i<n; i++)
		{
			j = findMinIndex(arr, i, n);
			tmp = arr[j];
			arr[j] = arr[i];
			arr[i] = tmp;
		}
		
	}

	static int findMinIndex(int[] arr, int start,int end){
		int min = start;
		int i = start+1;
		while(i<end)
		{
			if(arr[i]<arr[min]) min = i;

			i++;
		}

		return min;
	}
}