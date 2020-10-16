import java.util.*;

public class BubbleSort
{
	public static void main(String[] args)
	{
		Input input = new Input();

		int n = input.takeN();
		int[] arr = input.takeArray(n);

		bubbleSort(arr, n);

		input.afterSorting(arr);
		
		return;
	}

	static void bubbleSort(int[] arr, int n)
	{
		int tmp;
		for(int i=0; i<n; i++)
		{
			for(int j=i+1; j<n; j++)
			{
				if(arr[i] > arr[j])
				{
					tmp = arr[j];
					arr[j] = arr[i];
					arr[i] = tmp;
				}
			}
		}
		
	}
}