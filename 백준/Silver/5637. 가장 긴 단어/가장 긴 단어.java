import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        int maxLength = 0;
        String maxLengthString = "";

        while (!line.contains("E-N-D")) {

            int tempCount = 0;
            char[] tempString = new char[101];

            for (char c : line.toCharArray()) {
                if (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || c == '-') {
                    tempString[tempCount] = c;
                    tempCount++;
                }
                else {
                    if (tempCount > maxLength) {
                        maxLength = tempCount;
                        maxLengthString = String.valueOf(tempString);
                    }
                    tempCount = 0;
                    tempString = new char[101];
                }
            }

            tempCount = 0;
            tempString = new char[101];
            line = br.readLine();
        }

        System.out.println(String.valueOf(maxLengthString).substring(0, maxLength).toLowerCase());
    }
}
