import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        if (n % 2 == 1) sb.append(1);
        else sb.append(2);

        System.out.println(sb);
        br.close();
    }
}