import java.util.*;
import java.io.*;

/*
12869 뮤탈리스크

1.n 과 n개만큼의 SCV 체력을 입력 받는다.
2. dp를 이용해서 공격 회수의 최소값을 구한다.
3. 공격 횟수 출력
 */
public class Main {
    static int[] scv;
    static int n;
    static int[][][] dp = new int[61][61][61];
    static int[][] attack = {
            {9, 3, 1},
            {9, 1, 3},
            {3, 9, 1},
            {3, 1, 9},
            {1, 9, 3},
            {1, 3, 9}
    };

    static void dfs(int[] hp, int depth) {

        if (dp[hp[0]][hp[1]][hp[2]] <= depth) return;

        dp[hp[0]][hp[1]][hp[2]] = depth;
        for (int i=0; i<6; i++) {
            int[] newHp = {
                    Math.max(hp[0] - attack[i][0], 0),
                    Math.max(hp[1] - attack[i][1], 0),
                    Math.max(hp[2] - attack[i][2], 0)
            };
            dfs(newHp, depth+1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        scv = new int[3];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<3; i++) {
            scv[i] = i < n ? Integer.parseInt(st.nextToken()) : 0;
        }

        for (int i=0; i<61; i++) {
            for (int j=0; j<61; j++) {
                for (int k=0; k<61; k++) dp[i][j][k] = 100;
            }
        }

        dfs(scv, 0);
        System.out.println(dp[0][0][0]);
    }
}
