import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            String tempStr = st.nextToken();

            if (tempStr.equals("push")) {stack.push(Integer.parseInt(st.nextToken())); continue;}
            if (tempStr.equals("top")) sb.append(stack.empty() ? -1 : stack.peek());
            if (tempStr.equals("size")) sb.append(stack.size());
            if (tempStr.equals("empty")) sb.append(stack.empty() ? 1 : 0);
            if (tempStr.equals("pop")) sb.append(stack.empty() ? -1 : stack.pop());

            sb.append("\n");
        }

        System.out.println(sb.toString());
    }
}
