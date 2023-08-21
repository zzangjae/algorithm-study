import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static int[][] rooms = new int[15][15];

    public static void main(String[] args) throws FileNotFoundException, IOException {
        // BufferedReader bf = new BufferedReader(new InputStreamReader(new FileInputStream("src/input.txt")));
        int tcCount = Integer.parseInt(bf.readLine());

        for (int i=1; i<=14; i++){
            rooms[0][i] = i;
        }

        for (int i=1; i<=14; i++){
            for (int j=1; j<=14; j++){
                rooms[i][j] = rooms[i][j-1] + rooms[i-1][j];
            }
        }

        for (int i=1; i<=tcCount; i++){
            int k = Integer.parseInt(bf.readLine());
            int n = Integer.parseInt(bf.readLine());

            System.out.println(rooms[k][n]);
        }
    }
}
