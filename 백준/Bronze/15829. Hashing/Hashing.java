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
        int num;

        for (int i=0; i<input.length(); i++) {
            num = (int) input.charAt(i) - (int) 'a' + 1;
            result += (long) (num * Math.pow(R, i));
            result = result % M;
        }

        System.out.println(result);
    }
}