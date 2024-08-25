import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       int t = Integer.parseInt(br.readLine());
       StringBuilder sb = new StringBuilder();

        for (int i=0; i<t; i++) {

           StringTokenizer st = new StringTokenizer(br.readLine());
           n = Integer.parseInt(st.nextToken());
           m = Integer.parseInt(st.nextToken());
           
           for (int j=0; j<m; j++) {
               st = new StringTokenizer(br.readLine());
               int a = Integer.parseInt(st.nextToken()) - 1;
               int b = Integer.parseInt(st.nextToken()) - 1;
           }

           sb.append(n-1).append("\n");
        }

        System.out.println(sb);
    }
}