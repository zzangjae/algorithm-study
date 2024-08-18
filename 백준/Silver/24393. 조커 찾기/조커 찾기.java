import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int jokerIdx = 1;

        for (int i=0; i<n; i++) {
            String[] numSequence = br.readLine().split(" ");
            int newJokerIdx = 0;
            boolean isJokerInRight = jokerIdx > 13;
            jokerIdx = jokerIdx > 13 ? jokerIdx - 13 : jokerIdx;

            for (int j=0; j<numSequence.length; j++) {
                int num = Integer.parseInt(numSequence[j]);
                boolean isRight = j % 2 == 0;

                if ((isRight && isJokerInRight) || (!isRight && !isJokerInRight)) {
                    newJokerIdx += jokerIdx - num> 0 ? num : jokerIdx;
                    jokerIdx -= num;
                }
                else {
                    newJokerIdx += num;
                }
                
                if (jokerIdx <= 0) {
                    jokerIdx = newJokerIdx > 27 ? newJokerIdx - 27 : newJokerIdx;
                    break;
                }
            }
        }
        System.out.println(jokerIdx);
    }
}