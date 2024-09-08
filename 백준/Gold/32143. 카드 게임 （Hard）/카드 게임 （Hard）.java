import java.util.*;
import java.io.*;

/*
1. H를 입력 받고, N, Q를 입력 받는다. N개의 초기 카드와 이후 Q개의 카드를 입력 받는다.
2. priorityQue 에 카드를 큰 순대로 넣는다. 이때 상대 HP를 초과하면 더이상 넣지 않음
3. 새로운 카드가 들어올때마다 priorityQue 맨 위에 카드보다 숫자가 크면 priorityQue에 새로운 카드를 넣고
    HP 가 0 보다 커지기 직전까지 que 안에 있는 카드를 꺼낸다.
4. priorityQue 크기 출력
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int h = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), q = Integer.parseInt(st.nextToken());

        Queue<Integer> pq = new PriorityQueue<>();
        st = new StringTokenizer(br.readLine());
        int tempNum;
        long sum = 0;
        for (int i=0; i<n; i++) {
            tempNum = Integer.parseInt(st.nextToken());
            pq.add(tempNum);
            sum += tempNum;
        }

        StringBuilder sb = new StringBuilder();
        if (sum < h) sb.append(-1).append("\n");
        else {
            while (sum - pq.peek() >= h) {
                sum -= pq.poll();
            }
            sb.append(pq.size()).append("\n");
        }

        for (int i=0; i<q; i++) {
            tempNum = Integer.parseInt(br.readLine());
            sum += tempNum;
            pq.add(tempNum);
            if (sum < h) {
                sb.append(-1).append("\n");
            }
            else {
                while (sum - pq.peek() >= h) {
                    sum -= pq.poll();
                }
                sb.append(pq.size()).append("\n");
            }
        }

        System.out.print(sb);
    }
}
