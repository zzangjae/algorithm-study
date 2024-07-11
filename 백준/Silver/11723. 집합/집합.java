import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    private static class S {
        private HashSet<Integer> elements;

        public S() {
            elements = new HashSet<>();
        }

        public void add(int x) {
            if(check(x) == 0) elements.add(x);
        }

        public void remove(int x) {
            if(check(x) == 1) elements.remove(x);
        }

        public int check(int x) {
            if(elements.contains(x)) return 1;
            return 0;
        }

        public void toggle(int x) {
            if (check(x) == 1) remove(x);
            else add(x);
        }

        public void all() {
            for (int i=1; i<=20; i++) add(i);
        }

        public void empty() {
            elements.clear();
        }
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int M = Integer.parseInt(br.readLine());

        StringTokenizer st;
        S s = new S();
        StringBuilder sb = new StringBuilder();

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            String operation = st.nextToken();

            if (operation.equals("add")) s.add(Integer.parseInt(st.nextToken()));
            if (operation.equals("remove")) s.remove(Integer.parseInt(st.nextToken()));
            if (operation.equals("check")) {
                sb.append(s.check(Integer.parseInt(st.nextToken())) + "\n");
            }
            if (operation.equals("toggle")) s.toggle(Integer.parseInt(st.nextToken()));
            if (operation.equals("all")) s.all();
            if (operation.equals("empty")) s.empty();

        }

        System.out.println(sb.toString());
    }
}
