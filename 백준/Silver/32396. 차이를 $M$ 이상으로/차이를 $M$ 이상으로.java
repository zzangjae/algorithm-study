import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        final long INF = (long) Math.pow(10, 13);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long m = Long.parseLong(st.nextToken());

        long[] nums = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        int result = 0;
        for (int i=1; i<n; i++) {
            if (Math.abs(nums[i] - nums[i-1]) < m) {
                result++;
                nums[i] = INF;
            }
        }

        System.out.println(result);
    }
}
