import java.io.*;
import java.util.*;

/**
 * 14938 : 서강그라운드
 *
 * 1. n, m, r 입력 받기
 * 2. 각 구역의 아이템 수 배열로 입력 받기
 * 3. 모든 지역에서 플루이드 워샬 알고리즘을 통해 모든 노드로의 최단 경로를 구한다.
 * 4. 모든 지역에서에서 얻을 수 있는 item 수를 구하여 가장 큰 수를 출력한다.
 *
 */
public class Main {

    static int n;
    static int m;
    static int r;
    static int[][] distance;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        distance = new int[n][n];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                distance[i][j] = 100;
            }
            distance[i][i] = 0;
        }

        int[] items = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        for (int i=0; i<r; i++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken()) - 1;
            int end = Integer.parseInt(st.nextToken()) - 1;
            int roadLength = Integer.parseInt(st.nextToken());

            distance[start][end] = roadLength;
            distance[end][start] = roadLength;
        }

        for (int k=0; k<n; k++) {
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
                }
            }
        }

        int result = 0;
        for (int i=0; i<n; i++) {
            int maxItems = 0;

            for (int j=0; j<n; j++) {
                if (distance[i][j] <= m) maxItems += items[j];
            }

            result = Math.max(maxItems, result);
        }

        System.out.println(result);
    }
}
