import java.util.*;
import java.io.*;

/*
1. N 입력 받기, N개의 T, P 입력 받기
3. 다이나믹 프로그래밍 기법으로 한번 풀기
 */
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        class Counsel {
            public int period, cost;

            public Counsel(int period, int cost) {
                this.period = period;
                this.cost = cost;
            }
        }

        StringTokenizer st;
        Counsel[] reservation = new Counsel[n];
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            reservation[i] = new Counsel(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        int[] dp = new int[n+1];
        Stack<int[]> stack = new Stack<>();
        stack.add(new int[]{0, 0});

        while (!stack.isEmpty()) {

            int idx = stack.peek()[0];
            int costSum = stack.peek()[1];
            stack.pop();

            if (idx >= n) continue;

            if (idx + reservation[idx].period <= n && costSum + reservation[idx].cost > dp[idx + reservation[idx].period]) {
                dp[idx + reservation[idx].period] = costSum + reservation[idx].cost;
                stack.add(new int[] {idx + reservation[idx].period, costSum + reservation[idx].cost});
            }

            stack.add(new int[]{idx+1, costSum});
        }

        int result = 0;
        for (int i=0; i<=n; i++) {
            if (dp[i] > result) result = dp[i];
        }

        System.out.println(result);
    }
}
