import java.util.*;

public class QuickSort
{
	public static void main(String[] args)
	{
		Input input = new Input();

		int n = input.takeN();
		int[] arr = input.takeArray(n);

		quickSort(arr, 0, n-1);

		input.print(arr);
		
		return;
	}

	static void quickSort(int[] arr, int start, int end)
	{
		if(start < end)
		{
			int r = partition(arr, start, end);
			quickSort(arr, start, r-1);
			quickSort(arr, r+1, end);
		}
		
	}

	static int partition(int[] arr, int start, int end)
	{
		int p = arr[end];
		int i = start-1, tmp;
		for(int j=start; j<end; j++)
		{
			if(arr[j] < p){
				i++;
				tmp = arr[j];
				arr[j] = arr[i];
				arr[i] = tmp;
			}
		}
		arr[end] = arr[i+1];
		arr[i+1] =  p;

		return i+1;
	}
}