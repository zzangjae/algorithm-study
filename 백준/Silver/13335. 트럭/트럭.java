import java.util.*;
import java.io.*;

/*
13335 트럭
1. n, w, l 입력받고 배열로 i (0~n-1) 번째 트럭의 무게를 입력 받는다.
    각 트럭이 이동해야 할 거리를 w 로 초기화된 배열 이용
2.1 다리가 감당할 수 있는 무게만큼 right 오른쪽으로 1칸 이동 이동 할 떄마다 left ~ right 이동할 거리 1 감소 (시간 1 추가)
2.2 더이상 right가 오른쪽으로 이동할 수 없으면 다리 위에 모든 트럭이 대기 하고있는 상태이다.
    맨 왼쪽에 있는 이동해야 할 거리만큼 left ~ right 이동 할 거리 감소 (시간 맨 왼쪽 트럭이 이동할 만큼 추가)
2.3 left ~ right 중 이동할 거리가 0보다 작거나 같은 경우가 생기면
    left를 1칸 우측으로 이동한다.
3. 최종 시간 출력
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        int[] weight = new int[n];
        int[] position = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            weight[i] = Integer.parseInt(st.nextToken());
            position[i] = w+1;
        }

        int left = 0, right = 0, bridgeWeight = 0, time = 0;
        while (left < n) {

            // 2.1
            if (right < n && bridgeWeight + weight[right] <= l) {
                bridgeWeight += weight[right++];
                for (int i=left; i<right; i++) position[i]--;
                if (position[left] == 0) bridgeWeight -= weight[left++];
                time++;
                continue;
            }

            // 2.2
            time += position[left];
            for (int i=right-1; i>=left; i--) position[i] -= position[left];

            // 2.3
            bridgeWeight -= weight[left];
            left++;
            if (right < n && bridgeWeight + weight[right] <= l) {
                position[right]--;
                bridgeWeight += weight[right++];
            }
        }

        System.out.println(time);
    }
}
