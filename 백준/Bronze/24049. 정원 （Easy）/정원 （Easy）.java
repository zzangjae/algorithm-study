import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] garden = new int[n+1][m+1];

        st = new StringTokenizer(br.readLine());
        for (int r=1;  r<=n; r++) {
            garden[r][0] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int c=1; c<=m; c++) {
            garden[0][c] = Integer.parseInt(st.nextToken());
        }

        for (int i=1; i<=n; i++) {
            for (int j=1; j<=m; j++) {
                garden[i][j] = garden[i-1][j] == garden[i][j-1] ? 0 : 1;
            }
        }

        System.out.println(garden[n][m]);
    }
}