public class linearSearch {
    public static void main(String[] args) {
        Input input = new Input();    
        
        int n = input.takeN();
        int[] arr = input.takeArray(n);
        int key = input.takeKey();
        int i = 0;
        for(int ele: arr)
        {
            if(ele == key)
            {
                System.out.println("KEY FOUND AT INDEX "+i+1);
                return;
            }
            i++;
        }

        System.out.println("KEY NOT FOUND");
        return;
    }
}