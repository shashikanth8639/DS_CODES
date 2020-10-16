import java.util.*;

public class InsertionSort
{
	public static void main(String[] args)
	{
		Input input = new Input();

		int n = input.takeN();
		int[] arr = input.takeArray(n);

		insertionSort(arr, n);

		input.afterSorting(arr);
		
		return;
	}

	static void insertionSort(int[] arr, int n)
	{
		int i=1,j,tmp;
		while(i < n)
		{
			j = i;
			tmp = arr[i];
			while( j>0 && arr[j-1] > tmp)
			{
				arr[j] = arr[j-1];
				j--;
			}
			arr[j] = tmp;
			i++;
		}
	}
}