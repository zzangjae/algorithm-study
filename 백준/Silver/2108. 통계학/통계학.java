import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        int[] nums = new int[n];
        int sum = 0;
        int maxCount = 1;
        Map<Integer, Integer> numCount = new HashMap<>();

        for (int i=0; i<n; ++i) {
            int num = Integer.parseInt(bf.readLine());
            nums[i] = num;
            sum += num;
            if (!numCount.containsKey(num)){
                numCount.put(num, 1);
            }
            else{
                if (maxCount < numCount.get(num) + 1){
                    maxCount = numCount.get(num) + 1;
                }
                numCount.put(num, numCount.get(num)+1);
            }
        }

        if (sum < 0){
            System.out.println(Math.round(1.0 * sum /  n));
        }
        else{
            System.out.println(Math.round(1.0 * sum / n));
        }

        Arrays.sort(nums);
        System.out.println(nums[n / 2]);

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (Integer num: numCount.keySet()){
            if (numCount.get(num) == maxCount) pq.add(num);
        }

        int tempResult = pq.poll();
        if (pq.isEmpty()){
            System.out.println(tempResult);
        }
        else {
            System.out.println(pq.poll());
        }

        System.out.println(nums[n-1] - nums[0]);
    }
}
