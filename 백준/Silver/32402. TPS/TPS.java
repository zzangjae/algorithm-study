import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] direction = {
                {0, 1},
                {1, 0},
                {0, -1},
                {-1, 0}
        };
        int currentDirection = 0;

        int n = Integer.parseInt(br.readLine());

        int x = 0;
        int y = 0;
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            String input = br.readLine();

            if (input.equals("MR")) currentDirection = (currentDirection+1) % 4;
            if (input.equals("ML")) currentDirection = (currentDirection+3) % 4;

            int tempDirection = 0;
            if (input.equals("W")) {
                tempDirection = currentDirection;
            }
            if (input.equals("A")) {
                tempDirection = (currentDirection+3) % 4;
            }
            if (input.equals("S")) {
                tempDirection = (currentDirection+2) % 4;
            }
            if (input.equals("D")) {
                tempDirection = (currentDirection+1) % 4;
            }

            if (!input.equals("MR") && !input.equals("ML")) {
                x += direction[tempDirection][0];
                y += direction[tempDirection][1];
            }

            sb.append(x).append(" ").append(y).append(" ")
                    .append(x-direction[currentDirection][0]).append(" ")
                    .append(y-direction[currentDirection][1]).append(" ")
                    .append("\n");
        }

        System.out.println(sb);
    }
}
