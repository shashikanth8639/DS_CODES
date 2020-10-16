import javax.sound.midi.SysexMessage;
import java.util.Scanner;

public class HeapDemo {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements");
        int n = sc.nextInt();
        Heap heap1 = new Heap(n);
        Heap heap2 = new Heap(n);
        int ele;
        System.out.println("Enter the elements");
        for (int i = 0; i < n; i++) {
            ele = sc.nextInt();
            heap1.insert(ele);
            heap2.add(ele);
        }
        System.out.println(heap1);
        System.out.println(heap2);
        heap2.heapify();
        System.out.println(heap2);
        for (int i = 0; i < n; i++) {
            System.out.print(heap1.extract()+" ");
        }
        System.out.println();
        for (int i = 0; i < n; i++) {
            System.out.print(heap2.extract()+" ");
        }
        System.out.println();

    }
}
