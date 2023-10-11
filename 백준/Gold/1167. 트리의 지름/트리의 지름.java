import java.util.*;
import java.io.*;

public class Main {
    static int vCount;
    static ArrayList<HashMap<Integer, Integer>> tree;
    static boolean[] visited;
    static int maxDistance = 0;
    static int maxNode = 0;

    public static void dfs(int startNode, int distance){
        visited[startNode] = true;
        boolean isLastNode = true;

        for (Integer i: tree.get(startNode).keySet()){
            if ((tree.get(startNode).get(i) != 0) && !visited[i]){
                dfs(i, distance + tree.get(startNode).get(i));
                isLastNode = false;
            }
        }

        if (isLastNode && maxDistance < distance) {
            maxDistance = distance;
            maxNode = startNode;
        }

        visited[startNode] = false;
    }

    public static void main(String[] args) throws IOException, FileNotFoundException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        vCount = Integer.parseInt(st.nextToken());
        tree = new ArrayList<HashMap<Integer, Integer>>();
        visited = new boolean[vCount+1];

        for (int i = 0; i < vCount+1; i++) {
            tree.add(new HashMap<Integer, Integer>());
        }

        for (int i=0; i < vCount; i++) {
            st = new StringTokenizer(bf.readLine());
            int currentNode = Integer.parseInt(st.nextToken());

            while (true) {
                int connectNode = Integer.parseInt(st.nextToken());

                if (connectNode == -1)
                    break;

                tree.get(currentNode).put(connectNode, Integer.parseInt(st.nextToken()));
            }
        }

        dfs(1, 0);
        dfs(maxNode, 0);
        System.out.println(maxDistance);
    }
}