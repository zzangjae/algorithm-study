import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        int[] nums = new int[n];
        int tempSum = 0;

        for (int i=0; i<n; i++) {
            tempSum += Integer.parseInt(st.nextToken());
            nums[i] = tempSum;
        }

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(bf.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            if (s-2 < 0){
                System.out.println(nums[e-1]);
            }
            else System.out.println(nums[e-1] - nums[s-2]);
        }
    }
}