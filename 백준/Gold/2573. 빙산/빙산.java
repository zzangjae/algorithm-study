import java.io.*;
import java.util.*;

/**
 * 아이디어
 * 빙산이 분리 될 때 까지 빙산이 사라지는 로직을 수행하면 되는데,
 * 빙산이 분리 된 것은 dfs 와 빙산 개수를 이용하면 될 것 같다.
 * dfs 해서 갈 수 있는 곳이 숫자 빙산 개수보다 적으면 분리된 것으로 생각
 *
 * 구현
 * 1. n, m 입력 받기
 * 2. 빙산 현황 배열에 입력 받기 이 떄 빙산 개수 세어야 한다.
 * 3. 빙산이 1년 마다 없어지는 것을 구현. 이 떄 빙산이 없어진 뒤에 분리 되었는지 확인 해야 한다.
 */
public class Main {
    static int n;
    static int m;
    static int[][] ocean;
    static int icebergCount = 0;

    static int[][] direction = {
            {1, 0}, {0, 1}, {-1, 0}, {0, -1}
    };

    static boolean[][] visited;

    // 빙산이 분리되었는지 확인하는 함수 (DFS)
    static boolean isSeparated() {
        Stack<int[]> stack = new Stack<>();
        int tmpIcebergCount = 0;

        // 첫 번째 빙산의 위치를 찾음
        outerLoop:
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (ocean[i][j] != 0) {
                    stack.add(new int[]{i, j});
                    break outerLoop;
                }
            }
        }

        // 스택이 비어 있다면, 빙산이 전부 녹았으므로 바로 종료
        if (stack.isEmpty()) return true;

        // DFS로 탐색하면서 빙산 덩어리 개수를 셈
        while (!stack.isEmpty()) {
            int[] pos = stack.pop();
            int r = pos[0], c = pos[1];
            if (visited[r][c]) continue; // 이미 방문한 경우 스킵
            visited[r][c] = true;
            tmpIcebergCount++;

            for (int[] dir : direction) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && !visited[nr][nc] && ocean[nr][nc] != 0) {
                    stack.add(new int[]{nr, nc});
                }
            }
        }

        // 탐색한 빙산 덩어리 개수와 기존 빙산 개수가 다르면 분리된 것으로 판단
        return tmpIcebergCount != icebergCount;
    }
    // 1년 동안 빙산을 녹임
    static void advanceYear() {
        int[][] tempOcean = new int[n][m];

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (ocean[r][c] > 0) {
                    int iceberg = ocean[r][c];

                    // 4방향 탐색하여 주변 바다(0)의 개수만큼 빙산을 줄임
                    for (int[] dir : direction) {
                        int nr = r + dir[0], nc = c + dir[1];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m && ocean[nr][nc] == 0) {
                            iceberg = Math.max(0, iceberg - 1);
                        }
                    }

                    tempOcean[r][c] = iceberg;
                    if (iceberg == 0 && ocean[r][c] > 0) icebergCount--; // 녹아 없어지면 빙산 개수 감소
                }
            }
        }

        ocean = tempOcean; // 원래 ocean을 업데이트
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ocean = new int[n][m];
        visited = new boolean[n][m];

        // 빙산 정보 입력 및 빙산 개수 세기
        for (int r = 0; r < n; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < m; c++) {
                ocean[r][c] = Integer.parseInt(st.nextToken());
                if (ocean[r][c] > 0) icebergCount++;
            }
        }

        int result = 0;

        while (icebergCount > 0) { // 빙산이 존재할 동안 반복
            visited = new boolean[n][m]; // 매 년 방문 배열 초기화

            // 빙산이 분리되었는지 확인
            if (isSeparated()) {
                System.out.println(result);
                return;
            }

            // 1년 지나면서 빙산을 녹임
            advanceYear();
            result++;
        }

        // 빙산이 모두 녹았을 때도 분리되지 않으면 0 출력
        System.out.println(0);
    }
}
