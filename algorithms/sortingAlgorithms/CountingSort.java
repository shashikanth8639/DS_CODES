public class CountingSort
{
	public static void main(String[] args)
	{
		Input input = new Input();

		int n = input.takeN();
		int[] arr = input.takeArray(n);

		countingSort(arr, n);

		input.print(arr);
	}

	static void countingSort(int[] arr, int n)
	{
		int mix[] = minMax(arr, n);
		int min = arr[mix[0]];
		int max = arr[mix[1]];
		System.out.println(min+" "+max);
		int[] count = new int[max-min+1];

		for(int i=0; i<n;i++)
		{
			count[arr[i]-min] += 1;
		}
		int j = 0;
		for(int i=min;i<max+1;i++)
		{
			while(count[i-min] > 0)
			{
				arr[j] = i;
				j++;
				count[i-min]--;
			}
		}

	}
	static int[] minMax(int[] arr, int n)
	{
		int min=0,max=0;
		int[] mix = new int[2];
		for(int i=1;i<n;i++)
		{
			if(arr[i] < arr[min]) min = i;
			if(arr[i] > arr[max]) max = i;
		}
		mix[0] = min;
		mix[1] = max;
		return mix;
	}
}