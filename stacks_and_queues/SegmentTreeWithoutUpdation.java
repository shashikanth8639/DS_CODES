import java.util.*;

class SegmentTree
{
	int[] mins;
    int[] arr;
    int n;
	
	SegmentTree(int[] arr, int n)
	{
        this.arr = arr;
        this.n = n;
		mins = new int[2*n+1];
        initialize(1, 0, n-1);
	}

	public void initialize(int i, int start, int end)
	{
		if(start == end)
		{
			mins[i] = arr[start];
			return;
		}
		int mid = (start + end)/2;
		
		initialize(2*i, start, mid);
		initialize(2*i+1, mid+1, end);

		update(i);
	}

	public void update(int i)
	{
		mins[i] = Math.min( mins[2*i], mins[2*i+1]);
	}
	public int minimun(int a, int b)
	{
		return rangeMinimum(1, 0, n-1, a, b);
	}
    
	public int rangeMinimum(int i, int start, int end, int a, int b)
	{
		if ( b < start || a > end)
			return Integer.MAX_VALUE;

		if (a <= start && end <= b)
			return mins[i];

		int mid = (start + end)/2;

		int minLeft = rangeMinimum(2*i, start, mid, a, b);
		int minRight = rangeMinimum(2*i+1, mid+1, end, a, b);

		return Math.min(minLeft, minRight);

	}
}

public class SegmentTreeWithoutUpdation
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++)
        {
            arr[i] = sc.nextInt();
        }
        int a, b;
        SegmentTree st = new SegmentTree(arr, n);
        for(int i=0; i<q; i++)
        {
            a = sc.nextInt();
            b = sc.nextInt();
            System.out.println(st.minimun(a, b));
        }
        sc.close();
    }
}