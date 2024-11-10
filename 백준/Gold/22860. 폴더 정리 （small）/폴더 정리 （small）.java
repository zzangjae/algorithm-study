import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, ArrayList<String>> folders = new HashMap<>();
        HashMap<String, ArrayList<String>> files = new HashMap<>();

        for (int i=0; i<n+m; i++) {
            st = new StringTokenizer(br.readLine());
            String parent = st.nextToken();
            String child = st.nextToken();
            String isFolder = st.nextToken();

            if (isFolder.equals("1")) {
                folders.putIfAbsent(parent, new ArrayList<>());
                folders.putIfAbsent(child, new ArrayList<>());
                files.putIfAbsent(parent, new ArrayList<>());
                files.putIfAbsent(child, new ArrayList<>());
                folders.get(parent).add(child);
            }
            else {
                files.putIfAbsent(parent, new ArrayList<>());
                files.putIfAbsent(child, new ArrayList<>());
                files.get(parent).add(child);
            }
        }

        int q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<q; i++) {
            String[] folderPath  = br.readLine().split("/");
            String lastFolder = folderPath[folderPath.length-1];
            HashSet<String> fileSet = new HashSet<>();
            int fileCount = 0;

            Stack<String> stack = new Stack<>();
            stack.add(lastFolder);

            while(!stack.empty()) {
                String currentFolder =  stack.pop();
                stack.addAll(folders.get(currentFolder));

                for (String file: files.get(currentFolder)) {
                    fileSet.add(file);
                    fileCount++;
                }
            }

            sb.append(fileSet.size()).append(" ").append(fileCount).append("\n");
        };

        System.out.println(sb);
    }
}
