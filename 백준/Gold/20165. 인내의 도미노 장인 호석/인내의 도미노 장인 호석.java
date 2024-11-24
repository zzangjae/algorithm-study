import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];
        boolean[][] isFell = new boolean[n][m];

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] direction = {
                {-1, 0},
                {0, 1},
                {1, 0},
                {0, -1}
        };
        Map<String, Integer> directionMatcher = new HashMap<>();
        directionMatcher.put("N", 0);
        directionMatcher.put("E", 1);
        directionMatcher.put("S", 2);
        directionMatcher.put("W", 3);

        StringBuilder sb = new StringBuilder();
        int score = 0;
        for (int i=0; i<r; i++) {
            st = new StringTokenizer(br.readLine());
            int cr = Integer.parseInt(st.nextToken()) - 1;
            int cc = Integer.parseInt(st.nextToken()) - 1;
            int dr = directionMatcher.get(st.nextToken());

            if (isFell[cr][cc]) continue;

            int height = board[cr][cc];

            while (0 <= cr && cr < n && 0 <= cc && cc < m && height > 0) {
                if (!isFell[cr][cc]) {
                    isFell[cr][cc] = true;
                    score++;

                    if (height < board[cr][cc]) height = board[cr][cc];
                }

                cr += direction[dr][0];
                cc += direction[dr][1];
                height--;
            }

            st = new StringTokenizer(br.readLine());
            cr = Integer.parseInt(st.nextToken()) - 1;
            cc = Integer.parseInt(st.nextToken()) - 1;
            isFell[cr][cc] = false;
        }

        sb.append(score).append("\n");
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (isFell[i][j]) sb.append("F ");
                else sb.append("S ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
