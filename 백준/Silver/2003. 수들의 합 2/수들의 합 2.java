import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] A = new int[n];
        int[] prefixSum = new int[n+1];

        for (int i=0; i<n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            prefixSum[i+1] = A[i] + prefixSum[i];
        }

        int left = 0;
        int right = 1;
        int tempSum = 0;
        int answer = 0;

        while (left < n && right <= n) {
            tempSum = prefixSum[right] - prefixSum[left];

            if (tempSum == m) {
                answer++;
                left++;
            }

            if (tempSum > m) left++;

            if (tempSum < m) right++;
        }

        System.out.println(answer);
    }
}
