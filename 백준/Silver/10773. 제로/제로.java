import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws FileNotFoundException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> nums = new ArrayDeque<>();

        for (int i=0; i<k; i++){
            int num = Integer.parseInt(br.readLine());
            if (num != 0) nums.add(num);
            else nums.pollLast();
        }

        int result = 0;
        for (int num: nums){
            result += num;
        }

        System.out.println(result);
    }
}