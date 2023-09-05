import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException, FileNotFoundException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];

        for (int i=0; i<n; i++){
            nums[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(nums);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i=0; i<n; i++){
            bw.write(String.valueOf(nums[i]) + "\n");
        }

        bw.flush();
        bw.close();
    }
}