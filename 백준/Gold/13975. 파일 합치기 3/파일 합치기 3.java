import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<t; i++) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            PriorityQueue<Long> pq = new PriorityQueue<>();
            for (int j=0; j<n; j++) {
                pq.add(Long.parseLong(st.nextToken()));
            }

            long result = 0;
            while(pq.size() > 1) {
                long a = pq.poll();
                long b = pq.poll();

                result += a+b;
                pq.add(a+b);
            }

            sb.append(result).append("\n");
        }

        System.out.println(sb);
    }
}
