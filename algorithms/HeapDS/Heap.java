import java.util.Arrays;

public class Heap {
    int n, size;
    int[] arr;
    public Heap(int n){
        this.n = n;
        arr = new int[n+1];
        this.size = 1;
    }
    public void add(int ele){
        arr[size++] = ele;
    }
    public void insert(int ele){
        arr[size++] = ele;
        heapifyBottomToTop(size-1);
    }
    public void heapifyBottomToTop(int i){
        int tmp;
        while(i > 1){
            if(arr[i/2] > arr[i]){
                tmp = arr[i/2];
                arr[i/2] = arr[i];
                arr[i] = tmp;
            }
            i /= 2;
        }
    }
    public void heapifyTopToBotton(int i){
        int tmp, minChild;
        while(i*2 < size){
            minChild = minChild(i);
            if(arr[minChild] < arr[i]){
                tmp = arr[i];
                arr[i] = arr[minChild];
                arr[minChild] = tmp;
            }
            i = minChild;
        }
    }
    public int minChild(int i){
        if(i*2+1 >= size){
            return i*2;
        }
        if(arr[2*i] < arr[2*i+1]){
            return 2*i;
        }
        return 2*i+1;
    }
    public int extract(){
        int tmp = arr[1];
        arr[1] = arr[size-1];
        arr[size-1] = 0;
        size--;
        heapifyTopToBotton(1);
        return tmp;
    }
    public void heapify(){
        int i = n/2;
        while( i>0 ){
            heapifyTopToBotton(i);
            i--;
        }
    }

    @Override
    public String toString() {
        return "Heap{" +
                "n=" + n +
                ", size=" + (size-1) +
                ", arr=" + Arrays.toString(arr) +
                '}';
    }
}
