public class RadixSort
{
	public static void main(String[] args)
	{
		Input input = new Input();

		int n = input.takeN();
		int[] arr = input.takeArray(n);

		radixSort(arr, n);

		input.print(arr);
	}

	static void radixSort(int[] arr, int n)
	{
		int m = max(arr, n);
		int pos = 0;
		while(m>0)
		{
			pos += 1;
			countingSort(arr, pos, n);
			m = m/10;
		}

	}
	static void countingSort(int[] arr, int pos, int n)
	{

		int[] out = new int[n];
		int[] count = new int[10];
		int index;

		for(int i=0;i<n;i++)
		{
			index = getDigit(arr[i], pos);
			count[index] += 1;
		}
		for(int i=1;i<10;i++)
		{
			count[i] += count[i-1];
		}
		for(int i=n-1; i>=0; i--)
		{
			index = getDigit(arr[i], pos);
			out[count[index]-1] = arr[i];
			count[index]--;
		}
		for(int i=0;i<n;i++)
		{
			arr[i] = out[i];
		}
	}
	static int max(int[] arr, int n)
	{
		int max=arr[0];
		for(int i=1;i<n;i++)
		{
			if(arr[i] > max) max = arr[i];
		}
		return max;
	}

	public static int getDigit(int num, int pos)
	{
		String s = num+"";
		int n = s.length();
		if(pos<=n){
			return Character.getNumericValue(s.charAt(n-pos));
		}
		return 0;
	}
}