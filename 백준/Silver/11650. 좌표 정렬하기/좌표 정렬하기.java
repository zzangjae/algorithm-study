import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(bf.readLine());
        ArrayList<int[]> coordinate = new ArrayList<>();

        for (int i=0; i<n; i++){
            st = new StringTokenizer(bf.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            coordinate.add(new int[]{x, y});
        }

        Collections.sort(coordinate, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {

                if  (o1[0] == o2[0]){
                    return Integer.compare(o1[1], o2[1]);
                }

                else{
                    return Integer.compare(o1[0], o2[0]);
                }
            }
        });

        for (int[] pair: coordinate){
            System.out.print(pair[0]);
            System.out.print(" ");
            System.out.println(pair[1]);
        }
    }
}
