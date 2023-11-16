import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.valueOf(br.readLine());
        
        if (n % 2 == 0) {
            bw.write(String.format("%d is even", n));
        } else {
            bw.write(String.format("%d is odd", n));
        }
        
        bw.flush();
    }
}