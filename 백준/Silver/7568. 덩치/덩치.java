import java.util.*;
import java.io.*;

public class Main{

    public static void main(String args[]) throws IOException, FileNotFoundException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[][] personList = new int[n][2];

        for (int i=0; i<n; i++){
            st = new StringTokenizer(bf.readLine());
            personList[i][0] = Integer.parseInt(st.nextToken());
            personList[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i=0; i<n; i++){
            int rank = 1;

            for (int j=0; j<n; j++){
                if (personList[i][0] < personList[j][0] && personList[i][1] < personList[j][1]){
                    rank++;
                }
            }

            System.out.print(rank);
            System.out.print(" ");
        }
    }
}