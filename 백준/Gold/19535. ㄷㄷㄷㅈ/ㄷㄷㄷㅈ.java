import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st;
        long[] edgeCount = new long[n+1];
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        for (int i=0; i<n-1; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            edgeCount[a] += 1;
            edgeCount[b] += 1;

            map.computeIfAbsent(a, key -> new ArrayList<>());
            map.computeIfAbsent(b, key -> new ArrayList<>());
            map.get(a).add(b);
            map.get(b).add(a);
        }

        boolean[] visited = new boolean[n+1];

        long ㄷ = 0;
        long ㅈ = 0;

        for (int i=1; i<=n; i++) {
            if (edgeCount[i] >= 3) ㅈ += (edgeCount[i] - 2) * (edgeCount[i] - 1) * (edgeCount[i]) / 6;
        }

        for (int i=1; i<=n; i++) {

            visited[i] = true;

            for (int nextNode: map.get(i)) {
                if (!visited[nextNode] && edgeCount[nextNode] > 1 && edgeCount[i] > 1) {
                    ㄷ += (edgeCount[i]-1) * (edgeCount[nextNode]-1);
                }
            }
        }

        if (ㄷ > 3 * ㅈ) System.out.println("D");
        if (ㄷ < 3 * ㅈ) System.out.println("G");
        if (ㄷ == 3 * ㅈ) System.out.println("DUDUDUNGA");
    }
}
