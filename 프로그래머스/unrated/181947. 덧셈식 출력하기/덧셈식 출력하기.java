import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int a = Integer.valueOf(st.nextToken()), b = Integer.valueOf(st.nextToken());;
        
        bw.write(a + " + " + b + " = " + (a + b));
        bw.flush();
    }
}