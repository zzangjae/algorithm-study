import java.util.*;
import java.io.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        boolean[] visited = new boolean[n+1];

        ArrayList<String> result = new ArrayList<>();
        int idx = 0;

        for (int i=0; i<n; i++){
            int c = k;

            while (c > 0){
                if (idx+1 > n){
                    idx = 1;
                }
                else idx++;

                if (!visited[idx]) c--;
            }

            if (!visited[idx]) {
                result.add(String.valueOf(idx));
                visited[idx] = true;
            }
        }


        System.out.println("<" + result.stream().collect(Collectors.joining(", ")) + ">");
    }
}
