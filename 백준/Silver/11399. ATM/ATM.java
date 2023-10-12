import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int[] costs = new int[n];

        for (int i=0; i<n; i++){
            costs[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(costs);
        
        int tempSum = 0;
        int result = 0;
        
        for (int i=0; i<n; i++){
            tempSum += costs[i];
            result += tempSum;
        }
        
        System.out.println(result);
    }
}