import java.util.*;

public class MergeSort
{
	public static void main(String[] args)
	{
		Input input = new Input();

		int n = input.takeN();
		int[] arr = input.takeArray(n);
		if(n<0) return;
		merge(arr, 0, n-1);

		input.afterSorting(arr);
		
		return;
	}

	static void merge(int[] arr, int start, int end)
	{
		if(start < end)
		{
			int mid = (start + end)/2;

			merge(arr, start, mid);
			merge(arr, mid+1, end);

			mergeSort(arr, start, mid, end);
		}
		
	}

	static void mergeSort(int[] arr, int start, int mid, int end)
	{
		int[] left = new int[mid-start+1];
		for(int i=start;i<=mid;i++)
		{
			left[i-start] = arr[i];
		}

		int[] right = new int[end-mid];
		for(int i=mid+1;i<=end;i++)
		{
			right[i-mid-1] = arr[i];
		}

		int k=start, i=0,j=0;
		while(i<left.length && j<right.length)
		{
			if(left[i] > right[j])
			{
				arr[k++] = right[j++];
			}else{
				arr[k++] = left[i++];
			}
		}
		while(i<left.length)
		{
			arr[k++] = left[i++];
		}
		while(j<right.length)
		{
			arr[k++] = right[j++];
		}
	}
}