import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        final int R = 31;
        final int M = 1234567891;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String input = br.readLine();

        long result = 0;
        long num;
        long r;

        for (int i=0; i<input.length(); i++) {
            num = (int) input.charAt(i) - (int) 'a' + 1;

            r = 1;
            for (int j=0; j<i; j++) {
                r = (r * 31) % M;
            }

            result = (result + num * r) % M;
        }

        System.out.println(result);
    }
}
