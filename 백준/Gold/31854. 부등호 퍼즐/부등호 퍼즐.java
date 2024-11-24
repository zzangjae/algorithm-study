import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    static int[] board;
    static int[] depthCount;
    static List<List<Integer>> graph; // 그래프 간선 저장
    static int[] inDegree; // 진입 차수 배열
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n*n+1];
        depthCount = new int[n*n+1];
        graph = new ArrayList<>();
        inDegree = new int[n * n + 1];

        for (int i = 0; i <= n * n; i++) {
            graph.add(new ArrayList<>());
        }

        // 부등호 입력 처리 (가로 방향)
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n; j++) {
                int arg1 = i * n + j;
                int arg2 = i * n + j + 1;
                String sign = st.nextToken();

                if (sign.equals("<")) {
                    graph.get(arg1).add(arg2); // arg1 -> arg2
                    inDegree[arg2]++;
                } else {
                    graph.get(arg2).add(arg1); // arg2 -> arg1
                    inDegree[arg1]++;
                }
            }
        }

        // 부등호 입력 처리 (세로 방향)
        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                int arg1 = (i - 1) * n + j;
                int arg2 = i * n + j;
                String sign = st.nextToken();

                if (sign.equals("<")) {
                    graph.get(arg1).add(arg2); // arg1 -> arg2
                    inDegree[arg2]++;
                } else {
                    graph.get(arg2).add(arg1); // arg2 -> arg1
                    inDegree[arg1]++;
                }
            }
        }

        // 위상 정렬을 이용한 depth 계산
        topologicalSort();

        // depthCount를 누적하여 보드 값 계산
        for (int i = 1; i <= n * n; i++) {
            depthCount[board[i]]++;
        }

        for (int i = 1; i <= n * n; i++) {
            depthCount[i] += depthCount[i - 1];
        }

        for (int i = 1; i <= n * n; i++) {
            board[i] = depthCount[board[i]]--;
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= n; j++) {
                sb.append(board[i * n + j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    private static void topologicalSort() {
        Queue<Integer> queue = new LinkedList<>();

        // 진입 차수가 0인 노드부터 시작
        for (int i = 1; i <= n * n; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
                board[i] = 1; // 초기 depth 설정
            }
        }

        while (!queue.isEmpty()) {
            int curr = queue.poll();

            for (int next : graph.get(curr)) {
                inDegree[next]--;
                if (inDegree[next] == 0) {
                    queue.add(next);
                    board[next] = board[curr] + 1; // 현재 depth 기반으로 갱신
                }
            }
        }
    }
}
