import com.sun.source.tree.Tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        TreeMap<Integer, Integer> usingPort = new TreeMap<>();
        TreeSet<Integer> restingPort = new TreeSet<>();

        for (int i=1; i<=n; i++) {
            restingPort.add(i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i=1; i<=q; i++) {
            st = new StringTokenizer(br.readLine());
            int action = Integer.parseInt(st.nextToken());
            int portIdx = Integer.parseInt(st.nextToken());

            if (action == 1) {
                Integer tempPort;

                if (restingPort.contains(portIdx)) tempPort = portIdx;
                else tempPort = restingPort.higher(portIdx);

                if (tempPort == null) sb.append(-1).append("\n");
                else {
                    restingPort.remove(tempPort);
                    usingPort.put(tempPort, i);
                    sb.append(tempPort).append("\n");
                }
            }
            else {
                if (usingPort.containsKey(portIdx)) {
                    sb.append(usingPort.get(portIdx)).append("\n");
                    usingPort.remove(portIdx);
                    restingPort.add(portIdx);
                }
                else sb.append(-1).append("\n");
            }
        }

        System.out.println(sb);
    }
}
